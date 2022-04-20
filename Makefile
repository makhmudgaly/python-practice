# COLORS
GREEN := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE := $(shell tput -Txterm setaf 7)
RESET := $(shell tput -Txterm setaf sgr0)

VENV_CMD=. venv/bin/activate

help:
	@echo ''
	@echo 'Usage'
	@echo '	${YELLOW}make${RESET} ${GREEN}<target>${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-_0-9]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH);\
			printf "	${YELLOW}%-$(TARGET_MAX_CHAR_NUM)s${RESET} ${GREEN}%s${RESET}\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0}' $(MAKEFILE_LIST)
.PHONY: help

## Initialize venv
venv:
	@if [ ! -e "venv/bin/activate_this.py" ] ; then python3 -m venv venv; fi
.PHONY: venv
