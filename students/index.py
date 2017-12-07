DATA_FILE = 'student_files.csv'

def main():
    lineNum = 0
    with open(DATA_FILE, encoding='utf-8') as lines:
        for line in lines:
            if lineNum > 0:
                values = line.rstrip().split(',')
                if (values[2] < values[3] or values[2] < values[4] or
                values[5] < values[6] or values[5] < values[7] or
                values[8] < values[9] or values[8] < values[10] or
                values[11] < values[12] or values[11] < values[13] or
                values[14] < values[15] or values[14] < values[16]) :
                    print('Student name: ' + values[1] + ' ' + values[0])

                    # Concern
                    print('\tConcerning Courses:')
                    if values[2] < values[4]:
                        print('\t\tCurrent Math grade: ' + values[2] + ', ' + 'Warning Math grade: ' + values[4])
                    if values[5] < values[7]:
                        print('\t\tCurrent Math grade: ' + values[5] + ', ' + 'Warning Math grade: ' + values[7])
                    if values[8] < values[10]:
                        print('\t\tCurrent Math grade: ' + values[8] + ', ' + 'Warning Math grade: ' + values[10])
                    if values[11] < values[13]:
                        print('\t\tCurrent Math grade: ' + values[11] + ', ' + 'Warning Math grade: ' + values[13])
                    if values[14] < values[16]:
                        print('\t\tCurrent Math grade: ' + values[14] + ', ' + 'Warning Math grade: ' + values[16])

                    # Trouble
                    print('\tTrouble Courses:')
                    if values[2] < values[3]:
                        print('\t\tCurrent Math grade: ' + values[2] + ', ' + 'Objective Math grade: ' + values[3])
                    if values[5] < values[6]:
                        print('\t\tCurrent Math grade: ' + values[5] + ', ' + 'Objective Math grade: ' + values[6])
                    if values[8] < values[9]:
                        print('\t\tCurrent Math grade: ' + values[8] + ', ' + 'Objective Math grade: ' + values[9])
                    if values[11] < values[12]:
                        print('\t\tCurrent Math grade: ' + values[11] + ', ' + 'Objective Math grade: ' + values[12])
                    if values[14] < values[15]:
                        print('\t\tCurrent Math grade: ' + values[14] + ', ' + 'Objective Math grade: ' + values[15])
            lineNum += 1

main()
