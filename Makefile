# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jazurek <jazurek@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/14 22:31:40 by jazurek           #+#    #+#              #
#    Updated: 2026/08/14 22:43:08 by jazurek          ###   ########.fr        #
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
REQUIREMENTS_MAZE_GEN	:=	requirements_maze_gen.txt

MAZE_GEN_DIR			:=	maze_gen_build
MAZE_GEN				:=	maze_gen
LIB						:=	lib

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
	@$(VENV_PYTHON) -m pip install --quiet -r $(REQUIREMENTS_MAZE_GEN)


# Build maze_gen package
build: install-mazegen
	@echo "$(Green)[🛠 BUILDING]$(RESET) Building $(MAZE_GEN) package"
	@$(VENV_PYTHON) -m build $(MAZE_GEN_DIR) --quiet
	@cp -f $(MAZE_GEN_DIR)/dist/*.whl $(LIB)/


# Install dependencies
install: $(VENV_PYTHON) build
	@echo "$(MAGENTA)[🔗 INSTALL]$(RESET) Installing dependencies"
	@$(VENV_PYTHON) -m pip install --quiet --force-reinstall -r $(REQUIREMENTS)


# Run project
run: install
	@echo "$(GREEN)[🚀 RUNNING]$(RESET) Launching project"
	@$(VENV_PYTHON) $(ENTRY_POINT) $(CONFIG)


# Run with debugger
debug: install
	@echo "$(GREEN)[🦗 DEBUG]$(RESET) Launching debugger"
	@$(VENV_PYTHON) -m pdb $(ENTRY_POINT) $(CONFIG)


# Lint
lint: install
	@echo "$(CYAN)[🐒 LINT]$(RESET) Running flake8 and mypy"
	@$(VENV_PYTHON) -m flake8 . --extend-exclude=$(VENV)
	@$(VENV_PYTHON) -m mypy . $(MYPY_FLAGS) --exclude $(VENV)


# Optional strict lint
lint-strict: install
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


# Remove temporary files, mazegen package and virtual environment
fclean: clean
	@echo "$(YELLOW)[🧹 FCLEAN]$(RESET) Removing virtual environment"
	@rm -rf $(VENV)
	@rm -rf $(LIB)/$(MAZE_GEN)


# Reinstall
re: fclean install


.PHONY: all install run debug lint lint-strict clean fclean re
