default:

.PHONY: gen-help
gen-help: scripts/gen-help.sh
	@ bash "$<"

.PHONY: gen-init
gen-init: scripts/gen-init.sh
	@ bash "$<"
