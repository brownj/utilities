import commands

def get_password_from_keyring(account_name):
  cmd = "security find-generic-password -s " + account_name + " -w"
  (status, output) = commands.getstatusoutput(cmd)
  return output

 