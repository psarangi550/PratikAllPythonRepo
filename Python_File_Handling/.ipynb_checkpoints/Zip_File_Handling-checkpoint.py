{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fb8d055a",
   "metadata": {},
   "source": [
    "##### Here we need to write for the Zip File Handling \n",
    "##### The Main adv of Zip file is \n",
    "1. Handling of Zip file is easier than handling multiple files at a time as during the handing some misght miss or some might copied multiple times \n",
    "2. By the Zipping Memory utilisation will be imporved as we are compressiong the size\n",
    "3. Transportation will be rerally easy \n",
    "4. performance also be imporoved significantly \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8f190916",
   "metadata": {},
   "source": [
    "***For zipping and UnZipping Operation python provide inbuilt zipfile module***\n",
    "* here we need to import this inbuilt zipfile module \n",
    "* zipfile module has ZipFile Class for which we need to create the object to perform zipping and unzipping \n",
    "* we can use the same ZipFile class object for zipping and unzipping but there is a encoder to differenciate between both the operation\n",
    "* ZIP_DEFLATED:-specifying the zipping operation \n",
    "* ZIP_STORED:-specifying the unzipping operation:-By default present\n",
    "* for unzing ZIP_STORED is optional to mention but for zipping we must have to mention the ZIP_DEFLATED encoder while creating ZipFile Class Object\n",
    "    * for creating the zipfile for zipping operation\n",
    "    * z=ZipFile(\"name of the zip file\",\"w\",zipfile.ZIP_DEFLATED)#write mode\n",
    "    * for unzzing proced can be written as ZIP_STORED is optional \n",
    "    * z=ZipFile(\"name of the zip file\",\"r\",zipfile.ZIP_STORED)#read mode\n",
    "    * z=ZipFile(\"name of the zip file\",\"r\")#read mode\n",
    "###### for Zipping operation\n",
    "> * once the zipfile object created we can write the files to it in order to add the file to the zipfile \n",
    "> * we can use the zipfile obj.write(\"file we want to add to the zipFile Class object\") for the same \n",
    "\n",
    "   ###### for UnZipping operation\n",
    "    > * for unzipping and to display how many files insude it we can use the namelist()\n",
    "    > * this will provide the number of file exist in the zip File in the form of list \n",
    "    > * iterating the list we can file each file content \n",
    "    > * we can read the content and diplsya to the console \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "ffb6131b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import zipfile #importing the zipfile module\n",
    "#here we need to create 3 file and write some data into it \n",
    "f11=open(\"f11.txt\", \"w+\")#open the file in write mode\n",
    "f2=open(\"f2.txt\",\"w+\")#open the file in the write mode \n",
    "f3=open(\"f3.txt\",\"w+\")#open the file in the write mode\n",
    "print(f11.writable())\n",
    "f11.write(\"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\\n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\\n It has survived not only five centuries, but also the leap into electronic typesetting,\\n remaining essentially unchanged.\\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\\n and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\\n\")\n",
    "print(f11.readable())\n",
    "data=f11.read()\n",
    "print(data)\n",
    "f2.write(\"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\\n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\\n It has survived not only five centuries, but also the leap into electronic typesetting,\\n remaining essentially unchanged.\\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\\n and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\\n\")\n",
    "f3.write(\"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\\n when an unknown printer took a galley of type and scrambled it to make a type specimen book.\\n It has survived not only five centuries, but also the leap into electronic typesetting,\\n remaining essentially unchanged.\\n It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\\n and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\\n\")\n",
    "#here we need to create the ZipFile class object which present in zipfile module\n",
    "zipfileobj=zipfile.ZipFile(\"file_zip.zip\",\"w\",zipfile.ZIP_DEFLATED )\n",
    "#once the zipFile Object created we can write the files to that zip file by write(\"filename\") method\n",
    "zipfileobj.write(\"f11.txt\")\n",
    "zipfileobj.write(\"f2.txt\")\n",
    "zipfileobj.write(\"f3.txt\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "4f79f746",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\n",
      " when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
      " It has survived not only five centuries, but also the leap into electronic typesetting,\n",
      " remaining essentially unchanged.\n",
      " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n",
      " and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n",
      "\n",
      "\n",
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\n",
      " when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
      " It has survived not only five centuries, but also the leap into electronic typesetting,\n",
      " remaining essentially unchanged.\n",
      " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n",
      " and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n",
      "\n",
      "\n",
      "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\n",
      " when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n",
      " It has survived not only five centuries, but also the leap into electronic typesetting,\n",
      " remaining essentially unchanged.\n",
      " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,\n",
      " and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#for the unzipping also we can use the same Zip object \n",
    "from zipfile import ZipFile,ZIP_STORED\n",
    "import os #importing the os module to keep the same name\n",
    "#importing the encodeer as well as the ZipFile class in order to create ZipFile Class Object \n",
    "zip_obj=ZipFile(\"file112233_zip.zip\",\"r\",ZIP_STORED)#hrer creting the object of Zip File \n",
    "#but Remembr that ZIP_STORED is Present by default hence its completely optional \n",
    "#in order to see the file name insiode the xip file we can use the NameList() on the zipfile object\n",
    "list1=zip_obj.namelist()\n",
    "for l in list1:\n",
    "    fn,fext=os.path.splitext(l)\n",
    "    f=open(l,\"r+\")#open the fil;e in append mode \n",
    "    data=f.read()\n",
    "    print(data)\n",
    "    f.write(data)\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74a6a272",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ef0a0a10d58b4122b32c63d3f2c34a33",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(description='Ergebnis absenden', style=ButtonStyle())"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from ipywidgets import widgets, Button\n",
    "import requests\n",
    "btn = widgets.Button(description='Ergebnis absenden')\n",
    "\n",
    "display(btn);\n",
    "\n",
    "def submit_score(obj):\n",
    "    try:\n",
    "        if not endpoint or not uuid or not username:\n",
    "            raise RuntimeError(\"Parameters missing\");\n",
    "        elif not lm:\n",
    "            raise RuntimeError(\"LearningModule-Instance not as lm defined\")\n",
    "\n",
    "        score = lm.get_score();\n",
    "        taskEvaluationString = lm.get_task_evaluation_string();\n",
    "        response = requests.post(endpoint, data= {\"uuid\": uuid, \"grade\": score, \"username\": username, \"details\": taskEvaluationString })\n",
    "        if response.status_code != 200:\n",
    "            raise RuntimeError(\"Fehler beim Request: \" + str(response.status_code))\n",
    "    except RuntimeError as e:\n",
    "        print(e)\n",
    "    else:\n",
    "        print(\"Durchf??hrung erfolgreich abgegeben!\")\n",
    "btn.on_click(submit_score)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
