#!/usr/bin/env python3
"""Basic tests for the CLI module."""

import os
import subprocess
import sys

CLI = [sys.executable, "cli.py"]
CWD = os.path.dirname(__file__)


def run_cli(args):
    """Helper to run CLI with subprocess."""
    return subprocess.run(
        CLI + args,
        capture_output=True,
        text=True,
        cwd=CWD,
        )


def test_cli_help():
    """Test that the CLI shows help."""
    result = run_cli(["--help"])
    assert result.returncode == 0
    assert "101 Linux Commands CLI" in result.stdout


def test_hello_command():
    """Test the hello command."""
    result = run_cli(["hello", "greet"])
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout


def test_hello_command_with_name():
    """Test the hello command with a custom name."""
    result = run_cli(["hello", "greet", "--name", "Linux"])
    assert result.returncode == 0
    assert "Hello, Linux!" in result.stdout


def test_hello_help():
    """Test the hello command help."""
    result = run_cli(["hello", "--help"])
    assert result.returncode == 0
    assert "Hello command group" in result.stdout


# ----------------------------
# Tests for `show` subcommand
# ----------------------------

def test_show_ls():
    """Test the show command with ls."""
    result = run_cli(["show", "ls"])
    assert result.returncode == 0
    assert "# ls" in result.stdout or "Command: ls" in result.stdout
    assert "List" in result.stdout


def test_show_grep():
    """Test the show command with grep."""
    result = run_cli(["show", "grep"])
    assert result.returncode == 0
    assert "grep" in result.stdout
    assert "Search" in result.stdout or "Print" in result.stdout


def test_show_invalid():
    """Test the show command with an invalid command."""
    result = run_cli(["show", "foobar"])
    assert result.returncode == 1
    combined_output = result.stdout + result.stderr
    assert "Unknown command" in combined_output


if __name__ == "__main__":
    test_cli_help()
    test_hello_command()
    test_hello_command_with_name()
    test_hello_help()
    test_show_ls()
    test_show_grep()
    test_show_invalid()
    print("✅ All tests passed!")