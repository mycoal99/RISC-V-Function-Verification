from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import sys

# TODO: Read and understand this code. Write in your report a summary of what's happening in this code.
class RuleLearner():

    features = ['i3 = add','i3 = sub','i3 = mul','i3 = xor','v1>v2','v1<v2','v1=v2','v1 = random','v1 = large','v1 = medium','v1 = small','v1 = verysmall','v1 = 0x0000ffff','v1 = 0x00000000','v1 = 0xffffffff','v1 = 0xffff0000','v2 = random','v2 = large','v2 = medium','v2 = small','v2 = verysmall','v2 = 0x0000ffff','v2 = 0x00000000','v2 = 0xffffffff','v2 = 0xffff0000','v1 = pos','v1 = neg','v2 = pos','v2 = neg'] # TODO: Write, in order, the strings that map to your csv column features in here
    covers = ['COVERPOINT_ADD_UNSIGNED_OVERFLOW', 'COVERPOINT_ADD_SIGNED_OVERFLOW', 'COVERPOINT_SUB_NEGATIVE', 'COVERPOINT_MUL_ZERO', 'COVERPOINT_XOR_ZERO', 'COVERPOINT_XOR_ALL_ONES'] # TODO: Write, in order, the strings that map to your csv column classes in here

    def get_rules(self, cover_num, inputFile, outputFile):
        training_data = pd.read_csv(inputFile)
        cover_data = pd.read_csv(outputFile)
        feature_matrix = training_data[self.features].as_matrix()
        labels = cover_data[self.covers[cover_num]].as_matrix()

        clf = DecisionTreeClassifier(random_state=0)
        clf.fit(feature_matrix,labels)
        self.tree_to_code(clf, self.features)

    def tree_to_code(self, tree, feature_names):
        from sklearn.tree import _tree
        tree_ = tree.tree_
        feature_name = [
            feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
                for i in tree_.feature
        ]
        print("def tree({}):".format(", ".join(feature_names)))

        def recurse(node, depth):
            indent = "    " * depth
            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = feature_name[node]
                threshold = tree_.threshold[node]
                print("{}if {} <= {}".format(indent, name, threshold))
                recurse(tree_.children_left[node], depth + 1)
                print("{}else: # if {} > {}".format(indent, name, threshold))
                recurse(tree_.children_right[node], depth + 1)
            else:
                print("{}return {}".format(indent, tree_.value[node][0][0] < tree_.value[node][0][1]))

        recurse(0,1)

if __name__ =="__main__":
    rl = RuleLearner()
    cover_number = int(sys.argv[1])
    rl.get_rules(cover_number,"feature.csv","coverpoint.csv")
