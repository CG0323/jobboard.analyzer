# jobboard.analyzer
A python flask lighweight web service.  It is a subsystem of [__jobboard__](https://github.com/CG0323/jobboard) proejct
It acts as a background worker which analyzes the raw recruitment description, analyze required skills as well as the level 
of skills.Everytime a new recruiting post is sent to the backend, the analyze service will be triggered to process the text,
extract desired information from unstructured text and save the result into MySql data tables.

====