
from peakPickingTransformer import argument_parser
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

