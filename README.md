# SUSE Best Practices

A documentation series of best practices papers.


## Branches

| Name             | Purpose                                       |
|------------------|-----------------------------------------------|
| `main`           | doc development (latest development version)  |

**On Feb 20, 2021, we switched to a new default branch.**
**The default branch is now called `main`.**

**Use the *main* branch** as the basis of your commits/of new feature branches.


### How to update your local repository

If you *created* a local clone or GitHub fork of this repo *before Feb 20, 2021, do the following*:

```
git branch -m master main
git fetch origin
git branch -u origin/main main
git pull -r
```


## Contributing

Thank you for contributing to this repo. Please adhere to the following guidelines when creating a pull request:

* Make your pull request against the *main* branch if you are contributing to the most recent release. This branch is protected.

* Make sure all validation (Travis CI) checks are passed, and tag relevant SMEs from the development team (if applicable)
  and members of the SUSE Best Practices team: Meike Chabowski (@chabowski).

  **NOTE:** If your pull request has multiple files and reorganisation changes, please build locally using DAPS or daps2docker
  (see instructions below) to verify and build the files. Travis CI only validates, and does not ensure the XML builds
  are correct.

* Implement any required changes, or fix any merge conflicts if relevant. If you have any questions and are a SUSE employee, ping a documentation team member in #team-suse-docs on Slack.


## Editing DocBook

To contribute to the documentation, you need to write DocBook.

* You can learn about DocBook syntax at http://docbook.org/tdg5/en/html.
* SUSE documents are generally built with DAPS (package `daps`) and the
  SUSE XSL Stylesheets (package `suse-xsl-stylesheets`). Ideally, you should
  get these from the repository `Documentation:Tools`. However, slightly
  older versions are also available from the SLE and openSUSE repositories.


## Building documentation

If you are interested in building DAPS documentation (defaulting to HTML and PDF), you can utilize
either DAPS directly or use daps2docker. Both tools only work on Linux.

* Use daps2docker if you use any Linux distribution that includes Docker and Systemd and only want to
  build HTML, PDF, or EPUB and want to be set up as quickly as possible.
* Use DAPS directly if you are using a recent version of openSUSE, and want to use any of the advanced
  features of DAPS, such as building Mobipocket or spell-checking documents.


### Using daps2docker

1. Install Docker
2. Clone the daps2docker repository from https://github.com/openSUSE/daps2docker.
3. Within the cloned repository, run `./daps2docker.sh /PATH/TO/DOC-DIR`
   This builds HTML and PDF documents.


### Using DAPS directly

* `$ daps -d DC-<YOUR_BOOK> validate`: Make sure what you have written is well-formed XML and valid DocBook 5
* `$ daps -d DC-<YOUR_BOOK> pdf`: Build a PDF document
* `$ daps -d DC-<YOUR_BOOK> html`: Build multi-page HTML document

Learn more at https://opensuse.github.io/daps


## Published Documents

| DC File | Publication Status | Category | Product page links, comments |
| ------- | ------------------ | -------- | ---------------------------- |
| DC-CaaSP3-DataHub2 | ext | Container | https://documentation.suse.com/suse-caasp/4.0/, https://documentation.suse.com/sles-sap-12/, https://documentation.suse.com/sles-sap-15/ |
| DC-SAP_HA740_SetupGuide_AWS | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SAP_NW740_SLE12_SetupGuide | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SAP_NW740_SLE15_SetupGuide | ext | SAP | https://documentation.suse.com/sles-sap-15/ |
| DC-SAP_S4HA10_SetupGuide-SLE12 | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SAP_S4HA10_SetupGuide-SLE15 | ext | SAP | https://documentation.suse.com/sles-sap-15/ |
| DC-SBP-AMD-EPYC-2-SLES15SP1 | ext | ELS | https://documentation.suse.com/sles-15/ |
| DC-SBP-AMD-EPYC-SLES12SP3 | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-CloudLS-master | ext | Cloud Computing | https://documentation.suse.com/soc/9/, https://documentation.suse.com/soc/8/ |
| DC-SBP-DRBD | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-HANAonKVM-SLES12SP2 | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SBP-IaaS-SAP-Cloud | int | Cloud Computing | https://documentation.suse.com/soc/9/, https://documentation.suse.com/soc/8/ |
| DC-SBP-intelsupport | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-KMP-Manual | ext | ELS | https://documentation.suse.com/sles-12/, https://documentation.suse.com/sled-12/ |
| DC-SBP-KMP-Manual-SLE12SP2 | ext | ELS | https://documentation.suse.com/sles-15/, https://documentation.suse.com/sles-12/, https://documentation.suse.com/sled-15/, https://documentation.suse.com/sled-12/ |
| DC-SBP-Multi-PXE-Install | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-oraclerac | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-oracleweblogic | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-OracleWeblogic-SLES12SP3 | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-performance-tuning | ext | ELS | https://documentation.suse.com/sles-12/, https://documentation.suse.com/sles-15/ |
| DC-SBP-publiccloudinfra | ext | Cloud Computing | https://documentation.suse.com/soc/7/ |
| DC-SBP-Quilting-OSC | ext | Building Packages | https://documentation.suse.com/sles-12/ |
| DC-SBP-RPM-Packaging | ext | Sys Man | https://documentation.suse.com/sles-12/, https://documentation.suse.com/sles-15/ |
| DC-SBP-SAP-AzureSolutionTemplates | ext | SAP | https://documentation.suse.com/sles-sap-12/, https://documentation.suse.com/sles-sap-15/ |
| DC-SBP-SAP-HANA-PerOpt-HA-Azure | ext | SAP | https://documentation.suse.com/sles-sap-15/
| DC-SBP-SAP-MULTI-SID | ext | SAP | https://documentation.suse.com/sles-sap-15/
| DC-SBP-scominstallguide | ext | Sys Man | https://documentation.suse.com/suma/4.0/ |
| DC-SBP-scomusermanual | ext | Sys Man | https://documentation.suse.com/suma/4.0/ |
| DC-SBP-securitymodule | ext | ELS | https://documentation.suse.com/sles-11/ |
| DC-SBP-SLE15-Custom-Installation-Medium | ext | Sys Man | https://documentation.suse.com/sles-15/, https://documentation.suse.com/sled-15/ |
| DC-SBP-SLE-OffLine-Upgrade-Local-Boot | ext | Sys Man | https://documentation.suse.com/sles-15/, https://documentation.suse.com/sled-15/ |
| DC-SBP-SLES12SP1-SAP-migrationguide | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SBP-SLES-MFAD | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-Spectre-Meltdown-L1TF | ext | ELS | https://documentation.suse.com/sles-15/ plus all other SLE-based products |
| DC-SBP-strategy-short | int | Internal | [none] |
| DC-SBP-sumaforrhel | not published | Sys Man | [none, outdated] |
| DC-SBP-SUMA-on-IBM-PowerVM | ext | Sys Man | https://documentation.suse.com/suma/4.0/ |
| DC-SBP-susemanager | ext | Sys Man | https://documentation.suse.com/suma/4.0/ |
| DC-SLES12SP3-rpiquick | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SLES4SAP-hana-scaleOut-PerfOpt-12 | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SLES4SAP-hana-sr-guide-PerfOpt-12 | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SLES4SAP-hana-sr-guide-PerfOpt-12-Alicloud | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SLES4SAP-hana-sr-guide-PerfOpt-12_AWS | ext | SAP | https://documentation.suse.com/sles-sap-12/ |
| DC-SLES4SAP-hana-sr-guide-PerfOpt-15 | ext | SAP | https://documentation.suse.com/sles-sap-15/ |
| DC-SLES-rpiquick | ext | ELS | https://documentation.suse.com/sles-12/ |
| DC-SBP-Migrate-z-KVM | not published | Virt | [none, outdated] |
| DC-SBP-openFaaS | not published | ? | [none, unfinished, outdated] |


Papers not produced by documentation team which exist only as PDF (no DC file available) but need to be posted:

Category "SUSE Linux Enterprise Server for SAP"

* Setting up a SAP HANA SR Performance Optimized Infrastructure (SLES-SAP 11 SP4)
  https://www.suse.com/media/guide/sap_hana_sr_performance_optimized_scenario_11_sp4.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-11/

* Setting up a SAP HANA SR Cost Optimized Infrastructure (SLES-SAP 11 SP4)
  https://www.suse.com/media/guide/sap_hana_sr_cost_optimized_scenario_11_sp4.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-11/

* Setting up a SAP HANA SR Cost Optimized Infrastructure (SLES-SAP 12 SP1)
  https://www.suse.com/media/white-paper/sap_hana_sr_cost_optimized_scenario_12_sp1.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-12/

* Enqueue Replication - SAP NetWeaver High Availability on SUSE Linux Enterprise 12 (SP1 or newer)
  https://www.suse.com/media/guide/SLES4SAP-NetWeaver-ha-guide-EnqRepl-12_color_en.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-12/

* Simple Stack - SAP NetWeaver High Availability on SUSE Linux Enterprise 12 (SP1 or newer)
  https://www.suse.com/media/guide/simple_stack_sap_netweaver_high_availablity_on_suse_linux_enterprise_server_12.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-12/

* Operating System Security Hardening Guide for SAP HANA for SUSE Linux Enterprise Server 12
  https://www.suse.com/media/guide/operating_system_security_hardening_guide_for_sap_hana_for_suse_linux_enterprise_server_12.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-12/

* Operating System Security Hardening Guide for SAP HANA for SUSE Linux Enterprise Server 15
  https://www.suse.com/media/guide/Operatin_system_security_hardening_guide_for_sap_hana_for_suse_linux_enterprise_server_15.pdf
  also link from product page:
  https://documentation.suse.com/sles-sap-15/
