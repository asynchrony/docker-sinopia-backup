import json, sys, os, subprocess, time

src      = os.environ['BACKUP_SRC']
dest     = os.environ['BACKUP_DEST']
interval = float(os.environ['BACKUP_INTERVAL'])

while True:
  cmd = ["aws", "s3", "sync", src, dest, "--delete", "--exclude", "cache/*/*"]
  
  try:
        with open(os.path.join(src, "cache/.sinopia-db.json")) as data_file:
          data = json.load(data_file)
        for package in data["list"]:
          cmd.append("--include")
          cmd.append("cache/" + package + "/*")
  except IOError as e:
        print os.path.join(src, "cache/.sinopia-db.json") + " could not be found. Other files were still synced."
      
  code = subprocess.call(cmd)
  if code:
    sys.exit(code)

  time.sleep(interval)
