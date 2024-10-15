
from peakPickingTransformer import argument_parser
#Imports of large packages like pandas or torch take some time so, to make sure the --help command
#and argument validation happens quickly, we parse arguments before importing anything else.
args = argument_parser.Args()

from peakPickingTransformer.transformer_model import transformer

#parse mzML

if args.task == 'train':
    from peakPickingTransformer.utilities import load_training_data, split_data, assess_model
    #load and process training data
    X, Y = load_training_data(args)
    X_train, Y_train, X_test, Y_test = split_data(X, Y, args)
    
    #fit model
    model = transformer()
    model = model.fit(X_train, Y_train, args)
    model.dump(args)
    
    #make quality control plots
    assess_model(X_test, Y_test, model, args)   

elif args.task == 'refine':
    #initialize model
    model = transformer()
    model.load(args)

    #run GUI

elif args.task == 'infer':
    #initialize model
    model = transformer()
    model.load(args)

    #run inference

    #report results

