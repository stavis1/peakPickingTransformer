
from peakPickingTransformer import argument_parser
#Imports of large packages like pandas or torch take some time so, to make sure the --help command
#and argument validation happens quickly, we parse arguments before importing anything else.
args = argument_parser.Args()

from peakPickingTransformer.transformer_model import transformer

if args.task == 'train':
    from peakPickingTransformer.utilities import load_training_data, split_data, assess_model
    #load and process training data
    features = load_training_data(args)
    train_features, test_features = split_data(features, args)
    
    #fit model
    model = transformer()
    model = model.fit(train_features, args)
    model.dump(args)
    
    #make quality control plots
    assess_model(test_features, model, args)   

elif args.task == 'refine':
    #initialize model
    model = transformer()
    model.load(args)
    
    #parse mzML

    #run GUI

elif args.task == 'infer':
    #initialize model
    model = transformer()
    model.load(args)
    
    #parse mzML

    #run inference

    #report results

