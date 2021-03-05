#!/usr/bin/env bash

git describe --always --tags --dirty | sed -e 's/^v//'
