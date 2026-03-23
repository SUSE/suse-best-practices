#!/usr/bin/python3
"""
references.py
"""

import re

class Document:
    """ class document - scan a complete adoc document and all files included """

    def __init__(self, path):
        """ __init__(self,path) """
        self.path = path
        self.refs = {}     # {reference}
        self.vars = {}           # :variable: value

    def dscan(self):
        """ scan entire document """
        file = DocFile(self.path)
        file.fscan()

    def merge_references(self):
        """ merge references """

class DocFile:
    """ class doc_file - scan a single file and all includes """

    def __init__(self, path, **kargs):
        """ __init(self, path, **kargs) """
        self.path = path
        self.refs = {}     # {reference}
        self.vars = {}           # :variable: value
        self.lalala = kargs.get('lalala', None)

    def fscan(self):
        """ scan a single file """
        with open(self.path, "r", encoding="utf-8") as dfile:
            while line := dfile.readline():
                #print(line.rstrip())
                #
                # process include:: statements
                #
                match_obj = re.search("include::(.*)\[\]", line) # TODO: Migth need to process a reference as part of the path xxx{ref]xxx
                if match_obj:
                    self.process_include(match_obj)              # TODO: Check also for already included files to avoid loops and double includes
                #
                # process variable definitions (:VAR: VALUE)
                #
                match_obj = re.search("^:([^ ]*):(.*)", line)    # TODO: Is :VAR:VAL always at the begin (^) of the line?? 
                if match_obj:
                    self.process_variable_definition(match_obj)
                #
                # process references ( {ref} ) # TODO: also process multiple references: texttext{ref1}texttexttext{ref2}texttexttext
                #

    def process_include(self, match_obj):
        """ process a include operator """
        if match_obj:
            new_path = match_obj.group(1)
            print(f"INCLUDE: {self.path} -> {new_path}")
            new_file = DocFile(new_path)
            new_file.fscan()
            self.merge(new_file.vars, type='var')
            self.merge(new_file.refs, type='ref')

    def process_variable_definition(self, match_obj):
        """ process_variable_definition(self, match_obj) """
        if match_obj:
            # TODO: check, if var has already been defined (double or overwrite)
            new_var = match_obj.group(1)
            new_val = match_obj.group(2)
            self.merge({new_var: new_val}, type='var')
            # print(f"VAR {new_var} == {new_val}")   # TODO: Migth need to proccess reference on the right (value) side :var: VALVAL {ref} VALVAL

    def merge(self, merge_dict, **kargs):
         """ merge(self,merge_dict) - merges the given dictionary into self.refs or self.var """
         merge_type = kargs.get('type', 'var')
         if merge_type == 'var':
            merge_to = self.vars
         else:
            merge_to = self.refs
         for mt in merge_dict:
             mv = merge_dict.get(mt)
             if merge_to.get(mt):
                 print(f"WARNING: var {mt} has already been defined")
             else:
                 print(f"INFO: {self.path} var {mt} inserted (value {mv})")
                 merge_to.update({mt: merge_dict.get(mt)})

MY_PATH = "SLES4SAP-hana-sr-guide-PerfOpt-15.adoc"

my_doc = Document(MY_PATH)
my_doc.dscan()
