
from peakPickingTransformer import argument_parser
#Imports of large packages like pandas or torch take some time so, to make sure the --help command
#and argument validation happens quickly, we parse arguments before importing anything else.
args = argument_parser.Args()

from peakPickingTransformer.transformer_model import transformer

#parse mzML

if args.task == 'train':
    model = transformer()
    #load data
    #run training
    #report results    

elif args.task == 'refine':
    model = transformer()
    model.load(args)
    #run GUI

elif args.task == 'infer':
    model = transformer()
    model.load(args)
    #run inference
    #report results

