#!/usr/bin/python3
"""
references.py
"""

import argparse
import re
import sys
import time

class Document:
    """ class document - scan a complete adoc document and all files included """

    def __init__(self, path, **kargs):
        """ __init__(self,path, **kargs) """
        self.path = path
        self.refs = {}     # {reference}
        self.vars = {}     # :variable: value
        self.files = {}    # file included by
        self.exit = kargs.get('exit', False)
        # print(f"DBG self.exit = {self.exit}")

    def dscan(self):
        """ scan entire document """
        file = DocFile(self.path, files=self.files, vars=self.vars, exit=self.exit)
        file.fscan()

    def merge_references(self):
        """ merge references """

class DocFile:
    """ class doc_file - scan a single file and all includes """

    def __init__(self, path, **kargs):
        """ __init(self, path, **kargs) """
        self.path = path
        self.refs = {}     # {reference}
        self.vars = kargs.get('vars', {})
        self.files = kargs.get('files', {})
        self.exit = kargs.get('exit', False)
        # print(f"DBG self.exit = {self.exit}")

    def fscan(self):
        """ scan a single file """
        with open(self.path, "r", encoding="utf-8") as dfile:
            while line := dfile.readline():
                #print(line.rstrip())
                #
                # process include:: statements
                #
                # TODO: Migth need to process a reference as part of the path xxx{ref]xxx
                match_obj = re.search(r"include::(.*)\[\]", line)
                if match_obj:
                    # TODO: Check also for already included files to avoid loops and double includes
                    parent_file = self.files.get(match_obj.group(1))
                    if parent_file: 
                        print(f"ERROR: file {self.path} already included by {parent_file}")
                        if self.exit:
                            sys.exit(2)
                    else:
                        self.files.update({match_obj.group(1): self.path})
                        self.process_include(match_obj, files=self.files)
                #
                # process variable definitions (:VAR: VALUE)
                #
                # TODO: Is :VAR:VAL always at the begin (^) of the line??
                match_obj = re.search("^:([^ ]*) *: (.*)", line)
                if match_obj:
                    self.process_variable_definition(match_obj)
                #
                # process references ( {ref} )
                rest = line
                while rest:
                    match_obj = re.search("{([^}]*)}(.*$)", rest) # group1 should be the first reference, group2 is the rest of the line
                    if match_obj:
                        #print(f"Reference {match_obj.group(1)}")
                        rest = match_obj.group(2)
                        self.process_reference(match_obj.group(1))
                    else:
                        rest = None
                    #

    def process_include(self, match_obj, **kargs):
        """ process a include operator """
        self.files = kargs.get('files', {})
        if match_obj:
            new_path = self.resolve(match_obj.group(1))
            print(f"INCLUDE: {self.path} -> {new_path}")
            new_file = DocFile(new_path, files=self.files, vars=self.vars, exit=self.exit)
            new_file.fscan()
            #self.merge(new_file.vars, type='var', mode='overwrite')
            #self.merge(new_file.refs, type='ref')

    def process_variable_definition(self, match_obj):
        """ process_variable_definition(self, match_obj) """
        if match_obj:
            # TODO: check, if var has already been defined (double or overwrite)
            new_var = match_obj.group(1).rstrip()
            new_val = match_obj.group(2)
            # TODO: Migth need to proccess reference on the right (value) side
            #       :var: VALVAL {ref} VALVAL
            self.vars.update( {new_var.lower(): new_val} )
            # print(f"VAR <{new_var}> == <{new_val}>")

    def process_reference(self, reference):
        """ process_reference((self, reference) """
        if self.vars.get(reference.lower()) is None:
            print(f"WARNING: reference {reference} is used but not defined")
            if self.exit:
                sys.exit(2)
        else:
            val = self.vars.get(reference.lower())
            resolved_val = self.resolve(val)
            # print(f"INFO: reference {reference} is defined as '{val}' and resolves to '{resolved_val}'")

    def merge(self, merge_dict, **kargs):
        """ merge(self,merge_dict) - merges the given dictionary into self.refs or self.var """
        merge_type = kargs.get('type', 'var')
        merge_mode = kargs.get('mode', 'ignore')
        if merge_type == 'var':
            merge_to = self.vars
        else:
            merge_to = self.refs
        for mt in merge_dict:
            mv = merge_dict.get(mt)
            if merge_to.get(mt):
                print(f"WARNING: var {mt} has already been defined")
                if self.exit:
                    sys.exit(2)
                if merge_mode == "overwrite":
                    merge_to.update({mt: merge_dict.get(mt)})
            else:
                # print(f"INFO: {self.path} var {mt} inserted (value {mv})")
                merge_to.update({mt: merge_dict.get(mt)})

    def resolve(self, text, **kargs):
        """ reslve(self, text, kargs) """
        max_iteration = 20
        iteration = kargs.get('iteration', 0)
        iteration = iteration + 1
        # print(f"DEBUG: iteration {iteration}")
        #
        # replace all references e.g. ({node1})  by their value e.g.(suse01)
        rest = text
        while rest:
            match_obj = re.search("{([^}]*)}(.*$)", rest) # group1 should be the first reference, group2 is the rest of the line
            if match_obj:
                ref_var = match_obj.group(1)
                ref_val = self.vars.get(ref_var.lower(), "n/a") # TODO: report missing vars
                ref_ref = "{" + ref_var + "}"
                rest = match_obj.group(2)
                text = re.sub(ref_ref, ref_val, text, count=0, flags=0)
            else:
                rest = None
        #
        # check if by resolving new references have been added
        #
        match_obj = re.search("{([^}]*)}(.*$)", text) # group1 should be the first reference, group2 is the rest of the line
        if match_obj:
            if max_iteration >= iteration:
                text = self.resolve(text, iteration=iteration)
        return text
        
# MY_PATH = "SLES4SAP-hana-sr-guide-PerfOpt-15.adoc"

opt_exit=False

cmdline_parser = argparse.ArgumentParser()
cmdline_parser.add_argument("file", nargs="+", help="file(s) to be checked")
cmdline_parser.add_argument("--exit", help="stop on first warning or error", action="store_true")

args = cmdline_parser.parse_args()
if args.file:
    a_files = args.file
if args.exit:
    opt_exit = True

for my_path in a_files:
    my_doc = Document(my_path, exit=opt_exit)
    my_doc.dscan()
