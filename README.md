# Scientific Production with Spar Ontology Network
This is a repository with files and information generated during the research on the use of Spar Ontology Network for Scientific Production: Case study [University of Guayaquil](http://www.ug.edu.ec) in 2017 year.  
![spar-ug](https://user-images.githubusercontent.com/43136359/47797390-86829280-dd26-11e8-874f-42f4c4fa83b6.JPG)  
# Information
[Introduction](#Introduction)  
[Spar Ontology Network Brief](#Spar-Ontology-Network-Brief)  
[Obtaining DataSets ](#Obtaining-DataSets)  
[Relating and Cleaning Datasets](#Relating-and-Cleaning-Datasets)  
[Mapping Datasets](#Mapping-Datasets)  
[Transforming to RDF ](#Transforming-to-RDF)  
[Publishing RDF ](#Publishing-RDF)  
[Quering with SPARQL](#Quering-with-SPARQL) 

## Introduction
Universities are institutions where the research is a crucial piece to measure their prestige; hence, the importance to evaluate their scientific production. The [SPAR Ontology Network](http://www.sparontologies.net/) is a complete project to describe the scholarly publishing domain. We used the SPAR Ontology Network in order to check whether it is possible to represent the scientific production of universities. We selected the University of Guayaquil and its Scopus production in 2017 as a case study. The datasets were obtained from Scopus API in October 2018. Finally, we proposed ten competency question which was resolved using SPARQL.The next figure explain the process carried out. 
![process](https://user-images.githubusercontent.com/43136359/47798492-c185c580-dd28-11e8-9f58-8fc3d759ef75.JPG)

## Spar Ontology Network Brief
![spar ontologies](https://user-images.githubusercontent.com/43136359/48075146-d360e000-e1e2-11e8-81b7-e35b4593d894.jpeg)
  
### Ontologies for describing bibliographic resources and their parts
[FRBR-Aligned Bibliographic Ontology - FaBiO](http://purl.org/spar/fabio) records and publishes descriptions of textual publications that are published or potentially publishable (e.g., journals, conferences proceedings) and items of their content (e.g., articles, conference papers).  
[Essential FRBR in OWL2 DL - FRBR-DL](http://purl.org/spar/frbr)  represents the basic concepts and relations described in the International Federation of Library Associations and Institutions (IFLA) report on the Functional Requirements for Bibliographic Records (FRBR).  
[Document Components Ontology - DoCO](http://purl.org/spar/doco) provides a structured vocabulary of document components, both structural (e.g., paragraph, section, chapter) and rhetorical (e.g., introduction, discussion, reference list, figure, appendix).  
[Discourse Elements Ontology - DEO](http://purl.org/spar/deo) provides a structured vocabulary for rhetorical elements within documents (e.g., Introduction, Discussion, Acknowledgements, Reference List, Figures, Appendix).  
[DataCite Ontology - DataCite](http://purl.org/spar/datacite) provides a flexible mechanism to define identifiers (such as DOI, ISSN, ORCID.) for bibliographic resources (e.g., papers and datasets) and related entities (e.g., authors).  
### Ontologies for describing citations of scholarly resources  
[Citation Typing Ontology - CiTO](http://purl.org/spar/cito) characterises the bibliographic citations both factually and rhetorically. It seeks to capture the motivations of an author when referring to another document to be captured.  
[Bibliographic Reference Ontology - BiRO](http://purl.org/spar/biro) describes bibliographic records and references, and their compilation into bibliographic collections and reference lists.  
[Citation Counting and Context Characterization Ontology - C4O](http://purl.org/spar/c4o) allows the characterization of bibliographic citations regarding their number and their context.  
Two further supplementary ontologies have been made available to classify all the CiTO properties according to their factual and positive/neutral/negative rhetorical functions (FOCO, the Functions of Citations Ontology. ) and to map them with appropriate Wordnet synsets (C2W, the CiTO to Wordnet Ontology. ).  
### Ontologies for describing the publishing workflow
[Publishing Roles Ontology - PRO](http://purl.org/spar/pro) characterises the roles of agents (authors, editors, reviewers, publishers or librarians), corporate bodies and computational agents in the publication process.  
[Publishing Status Ontology - PSO](http://purl.org/spar/pso) characterises the publication status of documents at each stage of the publishing process (such as draft, submitted, under review).  
[Publishing Workflow Ontology - PWO](http://purl.org/spar/pwo) describes the steps in the workflow associated with the publication of a document or other publication entity.  
[Scholarly Contributions and Roles Ontology - SCoRO](http://purl.org/spar/scoro) extends PRO that describes the contributions that may be made, and the roles that may be held by a person concerning a journal article or other publication (e.g., the role of the illustrator).
[Funding, Research Administration and Projects Ontology - FRAPO](http://purl.org/cerif/frapo) describes the academic administrative information about grant funding and research projects, e.g., grant applications, funding bodies, project partners.  
[FAIR Reviews Ontology - FR](http://purl.org/spar/fr) defines a set of classes, properties and axioms, for describing research reviews as semantic objects, reusing standard existing vocabularies using ontology engineering techniques [15]. (It was recently added to the Spart Ontology Network).  
### Metrics and statistics for bibliographic resources  
[Bibliometric Data Ontology - BiDO](http://purl.org/spar/bido) allows the description of numerical and categorical bibliometric data concerning people, articles, journals, and other scholarly-related entities (e.g., journal impact factor, author h-index, categories describing research careers).  
[The Five Stars of Online Research Articles Ontology - FiveStars](http://purl.org/spar/fivestars) enables characterization of the five attributes of an online journal article - peer review, open access, enriched content, available datasets, and machine-readable metadata.  
## Obtaining DataSets 
Scopus has an API with allow to obtain data of papers, authors, journals, rankings, etc. We developed some Python scripts for calling Scopus services to obtain data from the University of Guayaquil.
## Relating and Cleaning Datasets 
We use MySQL and Open Refine to store and consolidate the data obtained in the previous step. The next figure shows the primary and foreing key of the entities that we used.
![mer](https://user-images.githubusercontent.com/43136359/47912233-2f043400-de98-11e8-8644-d63585c45c1e.JPG)
- Using MySQL we joined the tables: Papers, Papers-Authors, AuthorsUG, AuthorsNotUG, Source and Affiliations. The consolidate file has the follow column names: "paperId","authorid","Paper-Author","paperTitle","DocumentType","aggregationType","doi","url","ISSN1","ISSN2","ISBN","issue","volume","pageRange","coverDatePaper",year,"citationsPaper","ConferenceEdition","ConferenceName","CorrespondenceAddress","sourceID","sourceName","publisher","SJR","hindexJournal","authorName","affiliationID","nameAffiliation","country","docNumberAuthor","citationsAuthor","hindexAuthor","pubBeginning","pubEnd".
- Using Open refine we joined the tables: Area&Disciplines with Ranking2017 and obtained a project with the column names: "SourceID", "areaID", "area", "disciplineID", "discipline", "rank", "SJRQuartile".  
  
![mysql](https://user-images.githubusercontent.com/43136359/47915641-c9b64000-dea3-11e8-820f-69af18459cb1.JPG)  
  
## Mapping Datasets
For modeling the datasets into triples, we used the RDF extension from Open Refine. The RDF extension admits the reference of each component of the ontology to each column of data to be able to generate triplets. Some ontologies from the SPAR Ontology Network and other terms from well-known vocabularies were used to made the schema. 

## Transforming to RDF
Once the mapping of the data finished, that is when the columns of the table were related to its corresponding ontology term creating a schema, we proceeded to export an RDF file. 
```
<http://spar.linkeddata.es/60072042> a foaf:Organization ;  
	foaf:name "Universidad de Guayaquil" ;  
	schema:location "Ecuador" ;  
	foaf:member <http://spar.linkeddata.es/7202801165> ;  
	owl:sameAs "https://www.wikidata.org/wiki/Q7895474" .  
  
<http://spar.linkeddata.es/7202801165> a foaf:Person ;  
	foaf:name "Hernández F." ;  
	tvc:atTime <http://spar.linkeddata.es/7202801165-ProductionLife> ;  
	bido:holdsBibliometricDataInTime <http://spar.linkeddata.es/7202801165-2017> ;  
	dcterms:creator <http://spar.linkeddata.es/85005950245> .  
    
<http://spar.linkeddata.es/7202801165-ProductionLife> a time:Interval ;  
	time:hasBeginning <http://spar.linkeddata.es/1986-01-01> ;  
	time:hasEnd <http://spar.linkeddata.es/2016-12-31> .  
```
## Publishing RDF
For publishing the RDF, we employed the triple database [OpenLink Virtuoso](https://virtuoso.openlinksw.com/). The URI to access our endpoint to do any query to our data is http://spar.linkeddata.es/sparql, and the graph URI is http://spar.linkeddata.es/graph/ug.
## Quering with SPARQL
The competency questions and the queries is presented in this section. You can click in the play button to execute the query.  
### CQ1.   What kind of publication it is? 
```
prefix fabio:<http://purl.org/spar/fabio/>  
prefix dcterms: <http://purl.org/dc/terms/>  
prefix frbr: <http://purl.org/vocab/frbr/core/>  
  
SELECT DISTINCT ?y  
WHERE  
{  
?paper frbr:partOf ?source .  
?paper rdf:type ?y .  
?paper rdf:type fabio:Expression .   
}  
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2zUFw3z)

### CQ2.    What other organizations was the publication made with? 
```
prefix fabio:<http://purl.org/spar/fabio/>  
prefix dcterms: <http://purl.org/dc/terms/>  
prefix schema: <http://schema.org/>  
  
SELECT DISTINCT ?x ?y ?url ?country  
WHERE {  
?x foaf:name ?y .  
?x rdf:type foaf:Organization .   
?x schema:location ?country  
FILTER NOT EXISTS {?x foaf:name "Universidad de Guayaquil"}  
 OPTIONAL  
  { ?x owl:sameAs ?url . }  
}   
ORDER BY ?y   
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2OLQZYE)

### CQ3. What is the article's bibliographic metadata?
```
prefix fabio:<http://purl.org/spar/fabio/>   
prefix dcterms: <http://purl.org/dc/terms/>  
prefix frbr: <http://purl.org/vocab/frbr/core/>  
  
SELECT DISTINCT  ?x ?y ?z 
WHERE 
{  
   ?x ?y ?z .  
   ?x rdf:type fabio:BibliographicMetaData .  
   {  
       SELECT DISTINCT ?x  
       WHERE 
       {  
	   ?x frbr:realization ?y.  
	   ?y rdf:type fabio:Article. 
             {   
	       SELECT DISTINCT ?org  
	       WHERE  
	       {  
		   ?org foaf:name "Universidad de Guayaquil" .      
	       }  
	    }     
	}     
    }   
}  
ORDER BY ?x 
 
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2qPkz6g)

### CQ4. What is the conference paper’s bibliographic metadata?
```
prefix fabio:<http://purl.org/spar/fabio/>   
prefix dcterms: <http://purl.org/dc/terms/>  
prefix frbr: <http://purl.org/vocab/frbr/core/>  
  
SELECT DISTINCT  ?x ?y ?z 
WHERE 
{  
   ?x ?y ?z .  
   ?x rdf:type fabio:BibliographicMetaData .  
   {  
       SELECT DISTINCT ?x  
       WHERE 
       {  
	   ?x frbr:realization ?y.  
	   ?y rdf:type fabio:ConferencePaper. 
             {   
	       SELECT DISTINCT ?org  
	       WHERE  
	       {  
		   ?org foaf:name "Universidad de Guayaquil" .      
	       }  
	    }     
	}     
    }   
}  
ORDER BY ?x 

```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2DDefHv)

### CQ5. What is the book’s bibliographic metadata?
```
prefix fabio:<http://purl.org/spar/fabio/>   
prefix dcterms: <http://purl.org/dc/terms/>  
prefix frbr: <http://purl.org/vocab/frbr/core/>  
  
SELECT DISTINCT  ?x ?y ?z 
WHERE 
{  
   ?x ?y ?z .  
   ?x rdf:type fabio:BibliographicMetaData .  
   {  
       SELECT DISTINCT ?x  
       WHERE 
       {  
	   ?x frbr:realization ?y.  
	   ?y rdf:type fabio:BookChapter. 
             {   
	       SELECT DISTINCT ?org  
	       WHERE  
	       {  
		   ?org foaf:name "Universidad de Guayaquil" .      
	       }  
	    }     
	}     
    }   
}  
ORDER BY ?x 

 ```
 [![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2TfSWjB)
 
 ### CQ6. How many books, articles and conference papers researches have published?
```
prefix fabio:<http://purl.org/spar/fabio/>  
prefix dcterms: <http://purl.org/dc/terms/>  
SELECT * WHERE  
{  
    {  
        SELECT (COUNT(?x) AS ?Articles)   
        WHERE{?x rdf:type fabio:Article .}  
    }  
    UNION  
    {  
        SELECT (COUNT(?x) AS ?Books)   
        WHERE{?x rdf:type fabio:BookChapter .}  
    }  
    UNION  
    {  
        SELECT (COUNT(?x) AS ?Conferences)   
        WHERE{?x rdf:type fabio:ConferencePaper .}  
    }  
}  

```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2DFzUi2)

 ### CQ7. How many citations a researcher’s publication has received?
```
prefix fabio:<http://purl.org/spar/fabio/>    
prefix dcterms: <http://purl.org/dc/terms/>     
prefix bido: <http://purl.org/spar/bido-core/> 
prefix frbr: <http://purl.org/vocab/frbr/core/>    
  
SELECT DISTINCT ?valueCitations  ?title   
WHERE { 
?paper rdf:type fabio:Expression ;  
       bido:holdsBibliometricDataInTime ?paperMeasure .  
?bibliometricMetaData frbr:realization ?paper ;  
                      dcterms:title ?title .  
?paperMeasure bido:withBibliometricData ?citations .  
?citations bido:hasNumericValue ?valueCitations .  
}   
ORDER BY DESC(?valueCitations)  
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2FlAlj5)

### CQ8.   For how long a researcher has published?  
```
prefix time: <http://www.w3.org/2006/time#>  
prefix tvc: <http://www.essepuntato.it/2012/04/tvc/>  
prefix dcterms: <http://purl.org/dc/terms/>  

SELECT DISTINCT ?authorName  ?pubEnd ?dateBeginning ?dateEnd ?ProductionLifeYears  
WHERE  
{  
?author tvc:atTime ?authorPublicationLife .  
?authorPublicationLife rdf:type time:Interval ;  
                       time:hasBeginning ?pubBeginning ;  
                       time:hasEnd ?pubEnd .  
?pubBeginning time:inXSDDate ?dateBeginning .  
?pubEnd time:inXSDDate ?dateEnd.  
?org foaf:member ?author .  
?org foaf:name "Universidad de Guayaquil" .  
?author foaf:name ?authorName.  
bind( ?dateBeginning as ?start )  
bind( ?dateEnd as ?end )  
bind( year(?end)-year(?start) as ?ProductionLifeYears)  
}  
ORDER BY ?authorName
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2Dn6Db0)

### CQ9. How many researchers have published in Q1 (Quartile 1) journals and in which area?  
```
Not resolved  
```

### CQ10.  What is the h-index, number of citations and number of publications of a re-searcher?  
```
prefix fabio:<http://purl.org/spar/fabio/>  
prefix dcterms: <http://purl.org/dc/terms/>  
prefix bido: <http://purl.org/spar/bido-core/>  

SELECT DISTINCT ?authorName ?kind ?num  
WHERE  
{  
?author bido:holdsBibliometricDataInTime ?authorMeasure .  
?authorMeasure bido:withBibliometricData ?authorNum .  
?authorNum bido:hasMeasure ?kind ;  
          bido:hasNumericValue ?num.               
?org foaf:member ?author .  
?org foaf:name "Universidad de Guayaquil" .  
?author foaf:name ?authorName .   
}
ORDER BY ?authorName  
```
[![play](https://user-images.githubusercontent.com/43136359/47848297-3959fb80-ddce-11e8-8124-4f86d53d4d2a.png)](https://bit.ly/2PWXnkC)


[![DOI](https://zenodo.org/badge/155572685.svg)](https://zenodo.org/badge/latestdoi/155572685)  
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -   
Iconos play diseñados por [Smashicons](https://www.flaticon.es/autores/smashicons) desde [www.flaticon.com](https://www.flaticon.es/) con licencia [Creative Commons BY 3.0](http://creativecommons.org/licenses/by/3.0/)
