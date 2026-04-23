
# this makefile is to build the op reporter and the op reporter test
# it is not intended to be used by users, but by developers

DIRNAME := $(or $(word 2,$(MAKECMDGOALS)),.)
EXTRA_GOALS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
CONFIG_DIR ?= configs

$(EXTRA_GOALS):
	@:


run_op_reporter_test:
	python report_ops.py -jdir $(CONFIG_DIR)

rmreports:
	find $(DIRNAME) -type f -name "*master_report*.md" -delete 
	find $(DIRNAME) -type f -name "*master_report*.pdf" -delete 
	find $(DIRNAME) -type f -name "*master_report*.csv" -delete 
	find $(DIRNAME) -type f -name "*.operations*.md" -delete 
	find $(DIRNAME) -type f -name "*.operations*.pdf" -delete 
	find $(DIRNAME) -type f -name "*.operations*.csv" -delete 
	