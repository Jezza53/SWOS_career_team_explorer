import xml.dom.minidom
import binascii, argparse, subprocess
import os, glob
from dict import *
from func import *

def update_teamdata(datadirpath, outputdatapath, pattern='TEAM.0*'):
    directory_path = datadirpath
    hexoffset = 684                 # Each team has 684 bytes of data in TEAM.xxx file

    # Build a root of XML and info TAG
    XML_outputfile = xml.dom.minidom.parseString('<root/>')
    root = XML_outputfile.documentElement
    el_1 = XML_outputfile.createElement('info')
    el_1.setAttribute('tool', 'Autogenerated with SWOS Career Team Explorer by EMPI')
    root.appendChild(el_1)

    for TEAMxxx_file in glob.glob(directory_path + '/' + pattern):
        step = 0
        hexstart = 0x2+(hexoffset*step)
        divstart = 0x1b+(hexoffset*step)
        TEAMxxx_filesize = os.path.getsize(TEAMxxx_file)-1
        TEAMxxx_inputfile = open(TEAMxxx_file, 'r+b').read()
        
        # Declare TAG for current file as follows <TEAM.xxx country=xxx region=xxx career_playable=True/False>
        el_2 = XML_outputfile.createElement(os.path.basename(TEAMxxx_file))
        el_2.setAttribute('country_name', d_teamfile[os.path.basename(TEAMxxx_file)][0])
        el_2.setAttribute('region', d_teamfile[os.path.basename(TEAMxxx_file)][1])
        el_2.setAttribute('career_playable', str(d_teamfile[os.path.basename(TEAMxxx_file)][2]))
        root.appendChild(el_2)
        
        while hexstart <= TEAMxxx_filesize:
            el_3 = XML_outputfile.createElement(clear_4_XML(hexcutzeros(hexpure(hexread(TEAMxxx_inputfile,hexstart+0x5,16)))))
            el_3.setAttribute('club_name', hex2ascii(hexcutzeros(hexpure(hexread(TEAMxxx_inputfile,hexstart+0x5,16)))))
            el_3.setAttribute('hex_general_number', hexpure(hexread(TEAMxxx_inputfile,hexstart+0x2,2)))
            el_3.setAttribute('country_number', hexpure(hexread(TEAMxxx_inputfile,hexstart,1)))
            el_3.setAttribute('countryteam_number', hexpure(hexread(TEAMxxx_inputfile,hexstart+0x1,1)))
            el_3.setAttribute('division', hexpure(hexread(TEAMxxx_inputfile,divstart,1)))
            if hex2int(hexpure(hexread(TEAMxxx_inputfile,divstart,1))) < 4:
                el_3.setAttribute('career_playable', 'True')
            else:
                el_3.setAttribute('career_playable', 'False')
            el_2.appendChild(el_3)                
            
            step += 1
            hexstart = 0x2+(hexoffset*step)
            divstart = 0x1b+(hexoffset*step)

    open(outputdatapath + 'DATA_teams.xml',"w").write(XML_outputfile.toprettyxml())