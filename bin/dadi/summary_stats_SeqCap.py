#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python

"""
File: summary_stats_SeqCap.py
Author: Michael G. Harvey

Created by Michael G. Harvey on 21 September 2012
Copyright (c) 2012 Michael G. Harvey. All rights reserved.

Description: generate multi-population allele frequency spectra from SNPs from sequence capture
dataset and estimates summary statistics using dadi

Usage: python summary_stats_SeqCap.py

NOTE: This script depends on a modified version of the custom script "NeXus.py" written by 
R. Gutenkunst specifically for use with alignments in nexus format.

"""

import dadi
import NeXus_mod


"""
Generate frequency spectrum for 2 populations for xAndes.

"""    
    
    
if __name__ == '__main__':
    pop_assignments = {'Xenopsminutus025_CHa':'p1',
                       'Xenopsminutus025_CHb':'p1',
                       'Xenopsminutus102_SAa':'p2',
                       'Xenopsminutus102_SAb':'p2',
                       'Xenopsminutus103_NAa':'p2',
                       'Xenopsminutus103_NAb':'p2',
                       'Xenopsminutus104_CAa':'p1',
                       'Xenopsminutus104_CAb':'p1',
                       'Xenopsminutus110_CHa':'p1',
                       'Xenopsminutus110_CHb':'p1',
                       'Xenopsminutus111_SAa':'p2',
                       'Xenopsminutus111_SAb':'p2',
                       'Xenopsminutus118_NAa':'p2',
                       'Xenopsminutus118_NAb':'p2',
                       'Xenopsminutus119_CAa':'p1',
                       'Xenopsminutus119_CAb':'p1'
                       }


    # Generate data dictionary from NeXus alignment

    dd = NeXus_mod.data_dict_from_file('SeqCap_SNPs.nex', pop_assignments)
    
    # Generate frequency spectrum from data dictionary
    
    fs1 = dadi.Spectrum.from_data_dict(dd, ['p1'], [8], polarized=False)
    fs2 = dadi.Spectrum.from_data_dict(dd, ['p2'], [8], polarized=False)
    
    print "Population 1"
    theta1 = fs1.Watterson_theta()
    print theta1
    pi1 = fs1.pi()
    print pi1
    D1 = fs1.Tajima_D()
    print D1

    print "Population 2"
    theta1 = fs2.Watterson_theta()
    print theta1
    pi1 = fs2.pi()
    print pi1
    D1 = fs2.Tajima_D()
    print D1
