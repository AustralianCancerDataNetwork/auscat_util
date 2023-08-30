# Build command:    docker build -t auscat/pentaho-remove-conns:latest .
# Run command:      docker run --volume ./local/pentaho/directory/:/path/to/mount/to --env PATH_TO_PENTAHO_FILES=/path/to/your/mounted/folder auscat/pentaho-remove-conns:latest
# Example:          docker run --volume ./data:/projects/data --env PATH_TO_PENTAHO_FILES=/projects auscat/pentaho-remove-conns:latest
FROM python:3.7.16-slim-buster

ENV PATH_TO_PENTAHO_FILES placeholder

WORKDIR /projects

ADD ./reqs.txt .
RUN pip install -r reqs.txt
RUN pip install --upgrade pip

ADD ./auscatutil ./auscatutil
ADD ./remove_conn_strs_pentaho.py .

ENTRYPOINT python remove_conn_strs_pentaho.py ${PATH_TO_PENTAHO_FILES}
