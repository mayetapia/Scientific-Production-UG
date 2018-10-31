# Scientific-Production-UG
This is a repository with files generated during the research on the use of Spar Ontologies for Scientific Production: Case study [University of Guayaquil](http://www.ug.edu.ec).  
![spar-ug](https://user-images.githubusercontent.com/43136359/47797390-86829280-dd26-11e8-874f-42f4c4fa83b6.JPG)  
# Organization
[Introduction](#Introduction)  
[Obtaining DataSets ](#Obtaining-DataSets)  
[Related and Cleaning Datasets](#Related-and-Cleaning-Datasets)  
[Mapping Datasets](#Mapping-Dattasets)  
## Intoduction
Universities are institutions where the research is a crucial piece to measure their prestige; hence, the importance to evaluate their scientific production. [SPAR Ontology Network](http://www.sparontologies.net/) is a complete project to describe the scholarly publishing domain. We used Spar Ontology Network in order to inquire whether it is possible to represent the scientific production of the universities as well. We selected the University of Guayaquil as a case of study. The next figure explain the process carried out. 
![process](https://user-images.githubusercontent.com/43136359/47798492-c185c580-dd28-11e8-9f58-8fc3d759ef75.JPG)
## Obtaining DataSets 
Scopus has an API with allow to obtain data of papers, authors, journals, rankings, etc. We developed some Phyton scripts for calling Scopus services to obtain data from the University of Guayaquil.
## Related and Cleaning Datasets 
To store and consolidate data obtained in the previous step, we use a relational MySQL. The next figure shows the primary and foreing key of the entities that we used.
![mer2](https://user-images.githubusercontent.com/43136359/47802796-5f7d8e00-dd31-11e8-9fd0-5fc2b5a5d51b.JPG)
## Mapping Datasets
For modeling the datasets into triples, we used the RDF extension from Open Refine. We created two projects in Open Refine.  
- The first one relationed the tables: Papers, Papers-Authors, AuthorsUG, AuthorsNotUG, Source with the following column names: SourceID, paperID, authorID, affiliationID, documentType, aggregationType, paperTitle, datePaper, doi, url, issn, isbn, volume, issue,  pageRange, conferenceName, authorName, affililiationName, country,sourceName, publisher, country, sjr, journalHindex, authorHindex,  authorDocNumber, authorCitations, paperCitations, pubBegging, pubEnd.  
- The second one related the tables: Area&Disciplines with Ranking2017 with the following column names: SourceID, areaID, area, disciplineID, discipline, rank, SJRQuartile.  
