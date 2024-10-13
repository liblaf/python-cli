default:

.PHONY: gen-init
gen-init: scripts/gen-init.sh
	@ bash "$<"
