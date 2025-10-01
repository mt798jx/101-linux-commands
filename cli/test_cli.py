#!/usr/bin/env python3
"""Basic tests for the CLI module."""

import os
import subprocess
import sys

CWD = os.path.dirname(__file__)
PY = sys.executable
CLI = "cli.py"


def run_cli(args, *, check=True):
    """Helper to run the CLI with subprocess."""
    return subprocess.run(
        [PY, CLI, *args],
        capture_output=True,
        text=True,
        cwd=CWD,
        check=check,
    )


def test_cli_help():
    """Test that the CLI shows help."""
    result = subprocess.run(
        [PY, CLI, "--help"],
        capture_output=True,
        text=True,
        cwd=CWD,
        check=True,
    )
    assert result.returncode == 0
    assert "101 Linux Commands CLI" in result.stdout


def test_hello_command():
    """Test the hello command."""
    result = subprocess.run(
        [PY, CLI, "hello", "greet"],
        capture_output=True,
        text=True,
        cwd=CWD,
        check=True,
    )
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout


def test_hello_command_with_name():
    """Test the hello command with a custom name."""
    result = subprocess.run(
        [PY, CLI, "hello", "greet", "--name", "Linux"],
        capture_output=True,
        text=True,
        cwd=CWD,
        check=True,
    )
    assert result.returncode == 0
    assert "Hello, Linux!" in result.stdout


def test_hello_help():
    """Test the hello command help."""
    result = subprocess.run(
        [PY, CLI, "hello", "--help"],
        capture_output=True,
        text=True,
        cwd=CWD,
        check=True,
    )
    assert result.returncode == 0
    assert "Hello command group" in result.stdout


# ----------------------------
# Tests for `show` subcommand
# ----------------------------


def test_show_ls():
    """Test the show command with ls."""
    result = run_cli(["show", "ls"], check=True)
    assert result.returncode == 0
    out = result.stdout
    assert ("# ls" in out) or ("Command: ls" in out)
    assert "List" in out


def test_show_grep():
    """Test the show command with grep."""
    result = run_cli(["show", "grep"], check=True)
    assert result.returncode == 0
    out = result.stdout
    assert "grep" in out
    assert ("Search" in out) or ("Print" in out)


def test_show_invalid():
    """Test the show command with an invalid command."""
    result = run_cli(["show", "foobar"], check=False)
    assert result.returncode == 1
    combined_output = (result.stdout or "") + (result.stderr or "")
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
