# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"66h..00","system":"readv2"},{"code":"6AB..00","system":"readv2"},{"code":"E004.11","system":"readv2"},{"code":"Eu01100","system":"readv2"},{"code":"Eu02100","system":"readv2"},{"code":"Eu02200","system":"readv2"},{"code":"Eu02300","system":"readv2"},{"code":"Eu02400","system":"readv2"},{"code":"Eu02500","system":"readv2"},{"code":"ZS7C500","system":"readv2"},{"code":"2900","system":"oxmis"},{"code":"2901A","system":"oxmis"},{"code":"2901D","system":"oxmis"},{"code":"2919","system":"oxmis"},{"code":"2930","system":"oxmis"},{"code":"299 B","system":"oxmis"},{"code":"299 G","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('dementia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dementia-dementium---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dementia-dementium---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dementia-dementium---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
