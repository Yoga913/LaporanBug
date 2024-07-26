#!/bin/bash

# Pastikan pip sudah terinstall
if ! command -v pip &> /dev/null
then
    echo "pip tidak ditemukan, harap install pip terlebih dahulu."
    exit
fi

# Install paket yang diperlukan
pip install --upgrade pip setuptools wheel

# Install paket-paket spesifik
pip install --upgrade smtplib
pip install --upgrade email
pip install --upgrade templates
