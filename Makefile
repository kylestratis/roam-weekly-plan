PROJECT_DIR ?= $(shell pwd)
BUILD_DIR ?= $(PROJECT_DIR)/_build
ARCHIVE_DIR ?= $(BUILD_DIR)/archive
WORKFLOW_FILENAME ?= "RoamWeeklyPlan.alfredworkflow"
WORKFLOW_DIR ?= "$(PROJECT_DIR)/dist"
WORKFLOW_PATH ?= "$(WORKFLOW_DIR)/$(WORKFLOW_FILENAME)"
VERSION ?= $(shell $(PROJECT_DIR)/version.sh)

build: clean
	mkdir -p $(ARCHIVE_DIR) $(shell dirname "$(WORKFLOW_PATH)")
	cp -r $(PROJECT_DIR)/src/* $(ARCHIVE_DIR)/
	sed -i.bak 's/{{VERSION}}/$(VERSION)/g' $(ARCHIVE_DIR)/info.plist
	rm -f $(ARCHIVE_DIR)/info.plist.bak
	cd $(ARCHIVE_DIR) \
		&& zip $(WORKFLOW_PATH) * \
		&& echo "Created zip: $(WORKFLOW_PATH)"

clean:
	rm -rf $(BUILD_DIR) $(WORKFLOW_PATH)

version: ## output current version
	@echo $(VERSION)
