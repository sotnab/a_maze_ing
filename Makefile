# Escape characters
ESC				:=	$(shell printf '\033')
RESET			:=	$(ESC)[0m
DIM				:=	$(ESC)[2m

# Colors
BLACK			:=	$(ESC)[30m
RED				:=	$(ESC)[31m
GREEN			:=	$(ESC)[32m
YELLOW			:=	$(ESC)[33m
BLUE			:=	$(ESC)[34m
MAGENTA			:=	$(ESC)[35m
CYAN			:=	$(ESC)[36m
WHITE			:=	$(ESC)[37m

# Virtual environment name
VENV_NAME		:=	amz_venv
ENTRY_POINT		:=	a_maze_ing.py

# Project paths
SRC_PATH		:= ./src

# Python and mypy cache files
TEMP_FILES		:=	.mypy_cache \
					*/.mypy_cache \
					__pycache__ \
					*/__pycache__

# External libraries
REQUIREMENTS	:=	requirements.txt

# Mypy flags
MYPY_FLAGS		:=	--warn-return-any \
					--warn-unused-ignores \
					--ignore-missing-imports \
					--disallow-untyped-defs \
					--check-untyped-defs

MYPY_STRICT		:=	--strict

# Messages
CREATING_VENV	:=	Creating virtual environment
LAUNCH_VENV		:=	Run venv with: source ./$(VENV_NAME)/bin/activate
INSTALLING		:=	Installing dependencies
LAUNCHING		:=	Launching project
LAUNCHING_DEBUG	:=	Launching project in DEBUG mode
DELETING		:=	Deleting temp files
DELETING_FULL	:=	Deleting temp files and venv
LINTING			:=	Running flake8 and mypy
LINTING_STRICT	:= Running flake8 and mypy in STRICT mode

#  Rules
all: run

$(VENV_NAME):
	@echo "$(BLUE)[🛠️ CREATING VENV]$(RESET) $(WHITE)$(CREATING_VENV)$(RESET)"
	@python3 -m venv $(VENV_NAME)
	@echo "$(GREEN)[✨ SUCCESS]$(RESET) $(WHITE)$(LAUNCH_VENV)$(RESET)"

install: $(VENV_NAME)
	@echo "$(MAGENTA)[🔗 INSTALLING]$(RESET) $(WHITE)$(INSTALLING)$(RESET)"
	@. ./$(VENV_NAME)/bin/activate && pip install -r $(REQUIREMENTS)

run:
	@echo "$(GREEN)[🚀 RUNNING]$(RESET) $(WHITE)$(LAUNCHING)$(RESET)"
	@. ./$(VENV_NAME)/bin/activate && python3 $(ENTRY_POINT)

debug:
	@echo "$(GREEN)[🦗 DEBUG]$(RESET) $(WHITE)$(LAUNCHING_DEBUG)$(RESET)"
	@echo "$(BLUE) TODO $(RESET)"

clean:
	@echo "$(YELLOW)[🪣 CLEANING]$(RESET) $(WHITE)$(DELETING)$(RESET)"
	@rm -rf $(TEMP_FILES)

fclean:
	@echo "$(YELLOW)[🪣 FULL CLEANING]$(RESET) $(WHITE)$(DELETING_FULL)$(RESET)"
	@rm -rf $(TEMP_FILES) $(VENV_NAME)

lint:
	@echo "$(CYAN)[🐒 LINT]$(RESET) $(WHITE)$(LINTING)$(RESET)"
	@flake8 $(ENTRY_POINT) $(SRC_PATH)
	@mypy $(ENTRY_POINT) $(SRC_PATH) $(MYPY_FLAGS)

lint-strict:
	@echo "$(RED)[🦍 LINT]$(RESET) $(WHITE)$(LINTING_STRICT)$(RESET)"
	@flake8 $(ENTRY_POINT) $(SRC_PATH)
	@mypy $(ENTRY_POINT) $(SRC_PATH) $(MYPY_STRICT)

.PHONY: all install run debug clean fclean lint lint-strict
