import json, sys, os, subprocess, time

src      = os.environ['BACKUP_SRC']
dest     = os.environ['BACKUP_DEST']
interval = float(os.environ['BACKUP_INTERVAL'])

while True:
  cmd = ["aws", "s3", "sync", src, dest, "--delete", "--exclude", "cache/*/*"]
  
  if os.path.isfile(os.path.join(src, "cache/.sinopia-db.json")):
    with open(os.path.join(src, "cache/.sinopia-db.json")) as data_file:
      data = json.load(data_file)
    for package in data["list"]:
      cmd.append("--include")
      cmd.append("cache/" + package + "/*")

  code = subprocess.call(cmd)
  if code:
    sys.exit(code)

  time.sleep(interval)
