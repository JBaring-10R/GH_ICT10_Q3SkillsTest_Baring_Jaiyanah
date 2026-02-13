from pyscript import display, document  # type: ignore

def sign_up(e):
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    document.getElementById("output").innerHTML = ""

    if len(username) < 7:
        display("ᴜꜱᴇʀɴᴀᴍᴇ ᴀᴛ ʟᴇᴀꜱᴛ 7 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ. (｡•́︿•̀｡)", target="output")

    else:
        has_letter = False
        has_number = False

        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_number = True

        if len(password) < 10:
            display("ᴘᴀꜱꜱᴡᴏʀᴅ: ᴀᴛ ʟᴇᴀꜱᴛ 10 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ ʟᴏɴɢ. (｡•́︿•̀｡)", target="output")

        elif not has_letter:
            display("ᴘᴀꜱꜱᴡᴏʀᴅ: ᴀᴛ ʟᴇᴀꜱᴛ ᴏɴᴇ ʟᴇᴛᴛᴇʀ. (｡•́︿•̀｡)", target="output")

        elif not has_number:
            display("ᴘᴀꜱꜱᴡᴏʀᴅ: ᴀᴛ ʟᴇᴀꜱᴛ ᴏɴᴇ ɴᴜᴍʙᴇʀ. (｡•́︿•̀｡)", target="output")

        else:
            display("ᴄᴏɴɢʀᴀᴛꜱ! ʏᴏᴜ ʜᴀᴠᴇ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴍᴀᴅᴇ ᴀɴ ᴀᴄᴄᴏᴜɴᴛ. ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧", target="output")
