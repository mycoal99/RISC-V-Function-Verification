import randomFeatureChooser
import assemblyProgramFormatter
import Assembler
import csv
import os

def addUnsignedTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if v1neg <= 0.5:
        if v1rand <= 0.5:
            if i3mul <= 0.5:
                if i3add <= 0.5:
                    return False
                else: # if i3add > 0.5
                    if v2ffffffff <= 0.5:
                        if v1large <= 0.5:
                            if v2ffff0000 <= 0.5:
                                return False
                            else: # if v2ffff0000 > 0.5
                                if v10000ffff <= 0.5:
                                    return True
                                else: # if v10000ffff > 0.5
                                    return False
                        else: # if v1large > 0.5
                            if v1gtv2 <= 0.5:
                                return True
                            else: # if v1gtv2 > 0.5
                                return False
                    else: # if v2ffffffff > 0.5
                        return True
            else: # if i3mul > 0.5
                if v2neg <= 0.5:
                    if v2large <= 0.5:
                        return False
                    else: # if v2large > 0.5
                        if v10000ffff <= 0.5:
                            return False
                        else: # if v10000ffff > 0.5
                            return False
                else: # if v2neg > 0.5
                    if v100000000 <= 0.5:
                        if v1verysmall <= 0.5:
                            if v2medium <= 0.5:
                                return True
                            else: # if v2medium > 0.5
                                if v10000ffff <= 0.5:
                                    return True
                                else: # if v10000ffff > 0.5
                                    return False
                        else: # if v1verysmall > 0.5
                            return False
                    else: # if v100000000 > 0.5
                        return False
        else: # if v1rand > 0.5
            if i3mul <= 0.5:
                if v2verysmall <= 0.5:
                    if i3add <= 0.5:
                        if v1gtv2 <= 0.5:
                            if i3xor <= 0.5:
                                return False
                            else: # if i3xor > 0.5
                                return False
                        else: # if v1gtv2 > 0.5
                            return False
                    else: # if i3add > 0.5
                        if v2medium <= 0.5:
                            return True
                        else: # if v2medium > 0.5
                            return False
                else: # if v2verysmall > 0.5
                    return True
            else: # if i3mul > 0.5
                return True
    else: # if v1neg > 0.5
        if v1rand <= 0.5:
            if v1verysmall <= 0.5:
                return True
            else: # if v1verysmall > 0.5
                if v1eqv2 <= 0.5:
                    return True
                else: # if v1eqv2 > 0.5
                    if v2pos <= 0.5:
                        if i3mul <= 0.5:
                            return True
                        else: # if i3mul > 0.5
                            return True
                    else: # if v2pos > 0.5
                        return False
        else: # if v1rand > 0.5
            if i3sub <= 0.5:
                if v1eqv2 <= 0.5:
                    return True
                else: # if v1eqv2 > 0.5
                    if i3add <= 0.5:
                        return False
                    else: # if i3add > 0.5
                        return True
            else: # if i3sub > 0.5
                if v1eqv2 <= 0.5:
                    return False
                else: # if v1eqv2 > 0.5
                    return True

def addSignedTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if v1large <= 0.5:
        if v1rand <= 0.5:
            if i3add <= 0.5:
                if v20000ffff <= 0.5:
                    return False
                else: # if v20000ffff > 0.5
                    if v1medium <= 0.5:
                        return False
                    else: # if v1medium > 0.5
                        if i3mul <= 0.5:
                            return False
                        else: # if i3mul > 0.5
                            return True
            else: # if i3add > 0.5
                if v1medium <= 0.5:
                    if v1small <= 0.5:
                        return False
                    else: # if v1small > 0.5
                        if v1gtv2 <= 0.5:
                            if v2verysmall <= 0.5:
                                if v200000000 <= 0.5:
                                    return True
                                else: # if v200000000 > 0.5
                                    return False
                            else: # if v2verysmall > 0.5
                                return False
                        else: # if v1gtv2 > 0.5
                            return False
                else: # if v1medium > 0.5
                    if v1pos <= 0.5:
                        return True
                    else: # if v1pos > 0.5
                        return False
        else: # if v1rand > 0.5
            if i3add <= 0.5:
                if i3mul <= 0.5:
                    return False
                else: # if i3mul > 0.5
                    if v2ffffffff <= 0.5:
                        return True
                    else: # if v2ffffffff > 0.5
                        return False
            else: # if i3add > 0.5
                if v2medium <= 0.5:
                    if v1eqv2 <= 0.5:
                        return True
                    else: # if v1eqv2 > 0.5
                        if v1pos <= 0.5:
                            return True
                        else: # if v1pos > 0.5
                            return True
                else: # if v2medium > 0.5
                    return False
    else: # if v1large > 0.5
        if v1gtv2 <= 0.5:
            if i3xor <= 0.5:
                if i3sub <= 0.5:
                    return True
                else: # if i3sub > 0.5
                    return False
            else: # if i3xor > 0.5
                return False
        else: # if v1gtv2 > 0.5
            return False

def subNegativeTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if i3sub <= 0.5:
        return False
    else: # if i3sub > 0.5
        if v1ltv2 <= 0.5:
            if v1medium <= 0.5:
                if v1small <= 0.5:
                    if v1large <= 0.5:
                        if v1rand <= 0.5:
                            return False
                        else: # if v1rand > 0.5
                            if v2neg <= 0.5:
                                return True
                            else: # if v2neg > 0.5
                                if v2random <= 0.5:
                                    return True
                                else: # if v2random > 0.5
                                    return False
                    else: # if v1large > 0.5
                        if v1neg <= 0.5:
                            return True
                        else: # if v1neg > 0.5
                            return False
                else: # if v1small > 0.5
                    return True
            else: # if v1medium > 0.5
                return True
        else: # if v1ltv2 > 0.5
            if v2large <= 0.5:
                return True
            else: # if v2large > 0.5
                if v1small <= 0.5:
                    return True
                else: # if v1small > 0.5
                    if v1pos <= 0.5:
                        return False
                    else: # if v1pos > 0.5
                        return True

def mulZeroTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if i3mul <= 0.5:
        return False
    else: # if i3mul > 0.5
        if v200000000 <= 0.5:
            if v100000000 <= 0.5:
                if v1ffff0000 <= 0.5:
                    if v2verysmall <= 0.5:
                        return False
                    else: # if v2verysmall > 0.5
                        if v1neg <= 0.5:
                            return False
                        else: # if v1neg > 0.5
                            return False
                else: # if v1ffff0000 > 0.5
                    if v1eqv2 <= 0.5:
                        return False
                    else: # if v1eqv2 > 0.5
                        return True
            else: # if v100000000 > 0.5
                return True
        else: # if v200000000 > 0.5
            return True

def xorZeroTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if i3xor <= 0.5:
        return False
    else: # if i3xor > 0.5
        if v1eqv2 <= 0.5:
            return False
        else: # if v1eqv2 > 0.5
            return True

def xorOnesTree(i3add, i3sub, i3mul, i3xor, v1gtv2, v1ltv2, v1eqv2, v1rand, v1large, v1medium, v1small, v1verysmall, v10000ffff, v100000000, v1ffffffff, v1ffff0000, v2random, v2large, v2medium, v2small, v2verysmall, v20000ffff, v200000000, v2ffffffff, v2ffff0000, v1pos, v1neg, v2pos, v2neg):
    if v2ffffffff <= 0.5:
        return False
    else: # if v2ffffffff > 0.5
        if v100000000 <= 0.5:
            return False
        else: # if v100000000 > 0.5
            if i3sub <= 0.5:
                return True
            else: # if i3sub > 0.5
                return False


if __name__ == '__main__':
    featureObj = randomFeatureChooser.randomFeatureChooser()
    if os.path.exists('learnedFeature.csv') == 0:
        with open('learnedFeature.csv','w') as csv_file:
            writer = csv.writer(csv_file)
            delimiter = ','
            writer.writerow(featureObj.formatFirstCSVRow())
    learnedRules = 0
    while(learnedRules == 0):
        featureObj.csvFeatureArray = [0] * 29
        featureObj.generateRandomFeatureValues()
        featureObj.csvFeatureArray[featureObj.instructionFeatureType.index(featureObj.instructionFeature)] = 1
        featureObj.csvFeatureArray[4 + featureObj.comparisonFeatureType.index(featureObj.comparisonFeature)] = 1
        featureObj.csvFeatureArray[7 + featureObj.magnitudeFeatureType.index(featureObj.V1MagnitudeFeature)] = 1
        featureObj.csvFeatureArray[16 + featureObj.magnitudeFeatureType.index(featureObj.V2MagnitudeFeature)] = 1
        featureObj.csvFeatureArray[25 + featureObj.signFeatureType.index(featureObj.V1SignFeature)] = 1
        featureObj.csvFeatureArray[27 + featureObj.signFeatureType.index(featureObj.V2SignFeature)] = 1
        if addUnsignedTree(featureObj.csvFeatureArray[0],featureObj.csvFeatureArray[1],featureObj.csvFeatureArray[2],featureObj.csvFeatureArray[3],featureObj.csvFeatureArray[4],featureObj.csvFeatureArray[5],featureObj.csvFeatureArray[6],featureObj.csvFeatureArray[7],featureObj.csvFeatureArray[8],featureObj.csvFeatureArray[9],featureObj.csvFeatureArray[10],featureObj.csvFeatureArray[11],featureObj.csvFeatureArray[12],featureObj.csvFeatureArray[13], featureObj.csvFeatureArray[14],featureObj.csvFeatureArray[15],featureObj.csvFeatureArray[16],featureObj.csvFeatureArray[17],featureObj.csvFeatureArray[18],featureObj.csvFeatureArray[19],featureObj.csvFeatureArray[20],featureObj.csvFeatureArray[21],featureObj.csvFeatureArray[22],featureObj.csvFeatureArray[23],featureObj.csvFeatureArray[24],featureObj.csvFeatureArray[25],featureObj.csvFeatureArray[26],featureObj.csvFeatureArray[27],featureObj.csvFeatureArray[28]) == 1:
            learnedRules = 1
            assemblyProgramFormatter.instructionStore(featureObj)
            with open('learnedFeature.csv','a') as csv_file:
                writer = csv.writer(csv_file)
                delimiter = ','
                writer.writerow(featureObj.csvFeatureArray)
                featureObj.csvFeatureArray = [0] * 29