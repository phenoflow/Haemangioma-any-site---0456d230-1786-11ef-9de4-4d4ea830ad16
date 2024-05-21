# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"B7J0.00","system":"readv2"},{"code":"48140.0","system":"readv2"},{"code":"15185.0","system":"readv2"},{"code":"6525.0","system":"readv2"},{"code":"45686.0","system":"readv2"},{"code":"1969.0","system":"readv2"},{"code":"43321.0","system":"readv2"},{"code":"62001.0","system":"readv2"},{"code":"7363.0","system":"readv2"},{"code":"28527.0","system":"readv2"},{"code":"11719.0","system":"readv2"},{"code":"33366.0","system":"readv2"},{"code":"59737.0","system":"readv2"},{"code":"5100.0","system":"readv2"},{"code":"21598.0","system":"readv2"},{"code":"12281.0","system":"readv2"},{"code":"45969.0","system":"readv2"},{"code":"99715.0","system":"readv2"},{"code":"59746.0","system":"readv2"},{"code":"50658.0","system":"readv2"},{"code":"109447.0","system":"readv2"},{"code":"679.0","system":"readv2"},{"code":"43674.0","system":"readv2"},{"code":"61992.0","system":"readv2"},{"code":"4386.0","system":"readv2"},{"code":"65852.0","system":"readv2"},{"code":"33641.0","system":"readv2"},{"code":"4392.0","system":"readv2"},{"code":"22655.0","system":"readv2"},{"code":"1165.0","system":"readv2"},{"code":"50822.0","system":"readv2"},{"code":"36646.0","system":"readv2"},{"code":"17738.0","system":"readv2"},{"code":"15169.0","system":"readv2"},{"code":"94042.0","system":"readv2"},{"code":"101256.0","system":"readv2"},{"code":"531.0","system":"readv2"},{"code":"57570.0","system":"readv2"},{"code":"53774.0","system":"readv2"},{"code":"101861.0","system":"readv2"},{"code":"37117.0","system":"readv2"},{"code":"6185.0","system":"readv2"},{"code":"D18.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('haemangioma-any-site-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["haemangioma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["haemangioma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["haemangioma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
