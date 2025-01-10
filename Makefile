


# ==================================================================================== #
# HELPERS
# ==================================================================================== #


## help: print this help message
.PHONY: help
help:
	@echo 'Usage: '
	@sed -n 's/^##//p' ${MAKEFILE_LIST} | column -t -s ':' | sed -e 's/^/ /'

# ==================================================================================== #
# DEVELOPMENT
# ==================================================================================== #

## test: run the tests. Pass variable p=1 to run tests for a specific problem, otherwise runs all tests.
.PHONY: test
test:
ifdef p
	@pytest ./$(p)_*/test.py
else
	@pytest
endif