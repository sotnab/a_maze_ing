# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jazurek <jazurek@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/14 22:31:40 by jazurek           #+#    #+#              #
#    Updated: 2026/09/14 21:56:18 by jazurek          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Escape characters
ESC						:=	$(shell printf '\033')
RESET					:=	$(ESC)[0m
DIM						:=	$(ESC)[2m

# Colors
BLACK					:=	$(ESC)[30m
RED						:=	$(ESC)[31m
GREEN					:=	$(ESC)[32m
YELLOW					:=	$(ESC)[33m
BLUE					:=	$(ESC)[34m
MAGENTA					:=	$(ESC)[35m
CYAN					:=	$(ESC)[36m
WHITE					:=	$(ESC)[37m

# Project
PYTHON					:=	python3
VENV					:=	amz_venv
VENV_PYTHON				:=	$(VENV)/bin/python

ENTRY_POINT				:=	a_maze_ing.py
CONFIG					?=	config.txt
REQUIREMENTS			:=	requirements.txt
REQUIREMENTS_MAZEGEN	:=	requirements_mazegen.txt

MAZEGEN_DIR				:=	mazegen_src
MAZEGEN_DIST			:=	mazegen
MAZEGEN_WHEEL			:=	$(MAZEGEN_DIST)-0.1.0-py3-none-any.whl

MYPY_FLAGS				:=	--warn-return-any \
							--warn-unused-ignores \
							--ignore-missing-imports \
							--disallow-untyped-defs \
							--check-untyped-defs


all: run


# Create virtual environment
$(VENV_PYTHON):
	@echo "$(BLUE)[🛠️ VENV]$(RESET) Creating virtual environment"
	@$(PYTHON) -m venv $(VENV)


# Install dependencies for building mazegen package
install-mazegen: $(VENV_PYTHON)
	@echo "$(MAGENTA)[🔗 INSTALL]$(RESET) Installing mazegen dependencies"
	@$(VENV_PYTHON) -m pip install --quiet -r $(REQUIREMENTS_MAZEGEN)


# Build mazegen package
build: install-mazegen
	@echo "$(GREEN)[🛠 BUILDING]$(RESET) Building $(MAZEGEN_DIST) package"
	@rm -rf $(MAZEGEN_DIR)/build $(MAZEGEN_DIR)/dist
	@rm -rf $(MAZEGEN_DIR)/src/*.egg-info
	@$(VENV_PYTHON) -m build $(MAZEGEN_DIR) --quiet
	@cp -f $(MAZEGEN_DIR)/dist/$(MAZEGEN_WHEEL) ./


# Install dependencies
install: $(VENV_PYTHON) build
	@echo "$(MAGENTA)[🔗 INSTALL]$(RESET) Installing dependencies"
	@$(VENV_PYTHON) -m pip install --quiet --force-reinstall -r $(REQUIREMENTS)


# Run project
run:
	@echo "$(GREEN)[🚀 RUNNING]$(RESET) Launching project"
	@$(VENV_PYTHON) $(ENTRY_POINT) $(CONFIG)


# Run with debugger
debug:
	@echo "$(GREEN)[🦗 DEBUG]$(RESET) Launching debugger"
	@$(VENV_PYTHON) -m pdb $(ENTRY_POINT) $(CONFIG)


# Lint
lint:
	@echo "$(CYAN)[🐒 LINT]$(RESET) Running flake8 and mypy"
	@$(VENV_PYTHON) -m flake8 . --extend-exclude=$(VENV)
	@$(VENV_PYTHON) -m mypy . $(MYPY_FLAGS) --exclude $(VENV)


# Optional strict lint
lint-strict:
	@echo "$(RED)[🦍 LINT STRICT]$(RESET) Running strict checks"
	@$(VENV_PYTHON) -m flake8 . --extend-exclude=$(VENV)
	@$(VENV_PYTHON) -m mypy . --strict --exclude $(VENV)


# Remove temporary files
clean:
	@echo "$(YELLOW)[🧹 CLEAN]$(RESET) Removing temporary files"
	@find . -path "./$(VENV)" -prune -o \
		-type d \( -name "__pycache__" -o -name ".mypy_cache" -o -name ".pytest_cache" \) \
		-prune -exec rm -rf {} +
	@find . -path "./$(VENV)" -prune -o \
		-type f \( -name "*.pyc" -o -name "*.pyo" \) \
		-exec rm -f {} +


# Remove temporary files, build files and virtual environment
fclean: clean
	@echo "$(YELLOW)[🧹 FCLEAN]$(RESET) Removing virtual environment and build files"
	@rm -rf -- "$(VENV)"
	@rm -rf -- "$(MAZEGEN_DIR)/build"
	@rm -rf -- "$(MAZEGEN_DIR)/dist"
	@rm -rf -- "$(MAZEGEN_DIR)/src/"*.egg-info
	@rm -f -- "$(MAZEGEN_WHEEL)"


# Reinstall
re: fclean install


.PHONY: all install run debug lint lint-strict clean fclean re
