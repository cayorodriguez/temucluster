# TEMUcluster

## Descripcion

Creación de un archivo para clusterización en Carrot Workbench a partir de archivos en un directorio

The output is created as an XML file that can be loaded and visualized in the Carrot Workbench platform (https://doc.carrot2.org/):

<pre>
1. First it reads and opens text files from specified directory.

2. It convert eachdocument into an entry in an xml document formatted for Carrot, where the "snippet" is the text of the file, and its title and url are the filenames

3. The xml should be opened in Carrot WorkBench with the XML source option, and selecting a specific algorithm and the "read all documents from input" options. Then press "Process"

4. For each algorithm selected, it will open a tab, so be careful with the memory usage.

5. You can also select a keyword in the query field to create a clusterization with ONLY docs that contain that keyword
</pre>

## Resultado sobre un directorio de casos clínicos de oncología:

![Image of Clusterization](https://github.com/cayorodriguez/temucluster/blob/master/clusters-20200826164731.png)
