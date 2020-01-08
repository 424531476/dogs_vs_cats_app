import numpy as np
from keras.preprocessing import image
from keras.applications import InceptionV3, Xception, ResNet50, VGG16
from keras.applications import inception_v3, xception, resnet, vgg16
from keras.models import Model, Input
from keras.layers import Lambda, GlobalAveragePooling2D, Dense, concatenate


class NeuralNetwork:
    def __init__(self):
        def getmodel(model, preprocess_input=None, image_size=(299, 299, 3), output_layer=None, include_top=False):
            input_tensor = Input((image_size[0], image_size[1], image_size[2]))
            if preprocess_input:
                input_tensor = Lambda(preprocess_input)(input_tensor)
            base_model = model(input_tensor=input_tensor, weights='imagenet', include_top=include_top)
            output = base_model.output
            if output_layer is not None:
                output = base_model.layers[output_layer].output
            return Model(base_model.input, output)

        InceptionV3_model = getmodel(InceptionV3, inception_v3.preprocess_input)
        InceptionV3_ave_model = Model(InceptionV3_model.input,
                                      GlobalAveragePooling2D()(InceptionV3_model.output))

        Xception_model = getmodel(Xception, xception.preprocess_input)
        Xception_ave_model = Model(Xception_model.input,
                                   GlobalAveragePooling2D()(Xception_model.output))
        ResNet50_model = getmodel(ResNet50, resnet.preprocess_input)
        ResNet50_ave_model = Model(ResNet50_model.input,
                                   GlobalAveragePooling2D()(ResNet50_model.output))
        VGG16_model = getmodel(VGG16, vgg16.preprocess_input, output_layer=18)
        VGG16_ave_model = Model(VGG16_model.input,
                                GlobalAveragePooling2D()(VGG16_model.output))
        bottleneck_shape = (None,
                            int(InceptionV3_ave_model.output.shape[1] +
                                Xception_ave_model.output.shape[1] +
                                ResNet50_ave_model.output.shape[1] +
                                VGG16_ave_model.output.shape[1]))
        input_tensor = Input((bottleneck_shape[1],))
        x = input_tensor
        x = Dense(1, activation='sigmoid')(x)
        bottleneck_model = Model(input_tensor, x)
        bottleneck_model.load_weights('best_weights.hdf5')
        input_image = Input(shape=(299, 299, 3))
        concatenated = concatenate([InceptionV3_ave_model(input_image),
                                    Xception_ave_model(input_image),
                                    ResNet50_ave_model(input_image),
                                    VGG16_ave_model(input_image)],
                                   axis=1)

        self.model_merge = Model(input_image, bottleneck_model(concatenated))

    def predict(self, filenames):
        def load_image(img, image_size=(299, 299)):
            if type(img) == str:
                img = image.load_img(img, target_size=image_size)
                img = image.img_to_array(img)
                return np.expand_dims(img, axis=0)
            if isinstance(img, (tuple, list)):
                ret = [load_image(i) for i in img]
                return np.vstack(ret)

        image_tensor = load_image(filenames)
        return self.model_merge.predict(image_tensor)
