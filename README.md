droidboxhelper
==============

A slight modification to the DroidBox source and a helper file to convert the output into a more legible/readable form.

Usage
=====
Replace the scripts/droidbox.py file (for DroidBox 4.1.1) with the one provided in this repository or modify the code around line 512:

<pre>
  - print(json.dumps(output))
  - sys.exit(0)
  
  + print(json.dumps(output))
  + 
  + jsonhash = hashlib.sha1(json.dumps(output)).hexdigest()+'.json'
  + print 'Saving JSON data to file: '+jsonhash+'\n'
  + droidLog = open(jsonhash, 'w')
  + droidLog.write(json.dumps(output))
  + droidLog.close()
  + sys.exit(0)
</pre>

The result of the code modification is that DroidBox outputs the JSON to the screen but also saves it in a file where the file name is the hash of the data.  Then it is just a matter of running:
<pre>
  droidboxhelper.py hash.json
</pre>
