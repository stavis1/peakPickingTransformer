
from peakPickingTransformer import argument_parser
#Imports of large packages like pandas or torch take some time so, to make sure the --help command
#and argument validation happens quickly, we parse arguments before importing anything else.
args = argument_parser.args()


#parse mzML

if args.task == 'train':
    #initialize model
    #run training
    #report results    
    pass

elif args.task == 'refine':
    #initialize model
    #load weights
    #run GUI
    pass

elif args.task == 'infer':
    #initialize model
    #load weights
    #run inference
    #report results
    pass

