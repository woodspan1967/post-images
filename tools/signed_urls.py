"""Print 'dest url' queue lines for finished ElevenLabs generations.

usage: signed_urls.py dest1=generation_id1 dest2=generation_id2 ...
Finds each generation's signed content.png URL in this session's saved tool results
(~/.claude/projects/**/*.jsonl), newest match wins. Write the output to queue/<name>.txt and push;
the Fetch images workflow saves them under images/<dest> about a minute later.
"""
import glob, os, re, sys
text = ""
for f in sorted(glob.glob(os.path.expanduser("~/.claude/projects/**/*.jsonl"), recursive=True), key=os.path.getmtime):
    text += open(f, errors="ignore").read()
text = text.replace("\\u0026", "&").replace("\\\\", "\\")
for arg in sys.argv[1:]:
    dest, gid = arg.split("=", 1)
    urls = re.findall(r'https://storage\.googleapis\.com/[^"\\\s]*/' + re.escape(gid) + r'/content\.png\?[^"\\\s]+', text)
    if not urls: sys.exit(f"no URL found for {gid}; call creative_get_flow_run_status for it first")
    print(dest, urls[-1])
