import random
import threading
import multiprocessing
import shutil
import colorama
import requests
import sys
import os
from pystyle import Colors, Write
import time

logo = """
╔╦╗┌─┐┬┌─┌─┐┌┐┌╔═╗┌─┐┬─┐┌┬┐
 ║ │ │├┴┐├┤ │││║  │ │├┬┘ ││
 ╩ └─┘┴ ┴└─┘┘└┘╚═╝└─┘┴└──┴┘
"""
tokens = []

def LoadTitle(token_amount: int):
	return f"TokenCord - [Tokens: {token_amount}]"

def MainIntro():
	tokenfile = open("tokens.txt", "r", encoding="utf-8").read().split("\n")
	os.system(f'title {LoadTitle(len(tokenfile))}')
	

if __name__ == "__main__":
	pass
