# BJJ MerchDB
This is a simple static site that documents brands selling BJJ merchandise. 

**Building the dataset**  
The links were gleaned via manually traversing the sites and logging the respective URLs in a (not tracked) CSV. We then run `utils/builder.py` to serialize the CSV to JSON.  

**Considerations**  
Link rot, link rot, link rot...  

We have not chosen to implement a sophisticated answer to this issue such as gwern: [Archiving URLs](https://gwern.net/archiving).  

Instead, we have implemented a simple answer in `utils/health_checker.py` and `docs/form.html`.  

`health_checker.py` is manually run, reading in `docs/data.json` and iterating over the links. We make a request and check for a 200 OK, if another status code is returned we assume the link is dead and the URL value is blanked. The Google Form embedded in `form.html` allows for users to report new or broken links.  

### Potential Features
- tags eg $-$$$, currency, short shorts, etc
- sorting
- roll a form -> gcs, but probably not

### Running local_server
*Not tracked in git*  
`flask --app app --debug run`

### Build & Deploy
If there are changes to input data:  
1. cd into `utils`  
2. `python health_checker.py`  
3. `python builder.py`  
4. `git add docs/data.json`, commit, and push