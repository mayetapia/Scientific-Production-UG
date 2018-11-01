# Scientific-Production-UG
This is a repository with files generated during the research on the use of Spar Ontologies for Scientific Production: Case study [University of Guayaquil](http://www.ug.edu.ec).  
![spar-ug](https://user-images.githubusercontent.com/43136359/47797390-86829280-dd26-11e8-874f-42f4c4fa83b6.JPG)  
# Organization
[Introduction](#Introduction)  
[Obtaining DataSets ](#Obtaining-DataSets)  
[Related and Cleaning Datasets](#Related-and-Cleaning-Datasets)  
[Mapping Datasets](#Mapping-Datasets)  
[Transforming to RDF ](#Transforming-to-RDF)
[Publishing RDF ](#Publishing-RDF)
[Quering with SPARQL ](#Quering-with-SPARQL)
## Intoduction
Universities are institutions where the research is a crucial piece to measure their prestige; hence, the importance to evaluate their scientific production. [SPAR Ontology Network](http://www.sparontologies.net/) is a complete project to describe the scholarly publishing domain. We used Spar Ontology Network in order to inquire whether it is possible to represent the scientific production of the universities as well. We selected the University of Guayaquil as a case of study. The next figure explain the process carried out. 
![process](https://user-images.githubusercontent.com/43136359/47798492-c185c580-dd28-11e8-9f58-8fc3d759ef75.JPG)
## Obtaining DataSets 
Scopus has an API with allow to obtain data of papers, authors, journals, rankings, etc. We developed some Phyton scripts for calling Scopus services to obtain data from the University of Guayaquil.
## Related and Cleaning Datasets 
To store and consolidate data obtained in the previous step, we use a relational MySQL and Open Refine. The next figure shows the primary and foreing key of the entities that we used.
![mer2](https://user-images.githubusercontent.com/43136359/47802796-5f7d8e00-dd31-11e8-9fd0-5fc2b5a5d51b.JPG)  

- Using MySQL we joined the tables: Papers, Papers-Authors, AuthorsUG, AuthorsNotUG, Source2017. The consolide file has the follow column names: "paperId","authorid","Paper-Author","paperTitle","DocumentType","aggregationType","doi","url","ISSN1","ISSN2","ISBN","issue","volume","pageRange","coverDatePaper",year,"citationsPaper","ConferenceEdition","ConferenceName","CorrespondenceAddress","sourceID","sourceName","publisher","SJR","indexhJournal","authorName","AffiliationID","nameAffiliation","country","docNumberAuthor","citationsAuthor","hindexAuthor","pubBeginning","pubEnd".
- Using Open refine we joined the tables: Area&Disciplines with Ranking2017 and obtained a project with the column names: "SourceID", "areaID", "area", "disciplineID", "discipline", "rank", "SJRQuartile".  
## Mapping Datasets
For modeling the datasets into triples, we used the RDF extension from Open Refine. We created two projects in Open Refine. We called the first one "Union" and the second one "Ranking2017". With Spar Ontology was possible mapping the first one project but the second one we did not found class and propoertys for respresentation of area of study, discipline of area of study and quartile.  
## Transforming to RDF
Open Refine allows downloading a file in RDF/XML or RDF Turtle format. We chose the last one as it is a format accessible to read for humans as it is showed in the next figure.  
![rdf extract](https://user-images.githubusercontent.com/43136359/47806467-2564ba00-dd3a-11e8-8fdb-655609c93f93.JPG)
## Publishing RDF
For publishing the RDF, we employed the triple database OpenLink Virtuoso. The URI to access our endpoint to do any query to our data is http://sandbox.linkeddata.es/sparql, and the graph URI is http://sandbox.linkeddata.es/graph/mariela.
## Quering with SPARQL
The competency questions and the query is presented in this section. You can click in the link to execute the query.  
### CQ1.   What kind of publication it is? 
prefix fabio:<http://purl.org/spar/fabio/>  
prefix dcterms: <http://purl.org/dc/terms/>  
  
SELECT DISTINCT ?y  
WHERE  
{ ?x rdf:type ?y .  
?x rdf:type fabio:Expression .  
}  
[Execute](https://bit.ly/2OZm40c)
[![play](https://user-images.githubusercontent.com/43136359/47846487-4aa00980-ddc8-11e8-8f35-71cd370ce390.png)](https://bit.ly/2OZm40c)
[<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)

[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)


