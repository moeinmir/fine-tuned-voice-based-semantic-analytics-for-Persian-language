# Fine Tuned Voice Based Semantic Analytics For Persian Language



```
mkdir data/shemo
```

##### Down load data set

##### Download the dataset

From this repo: [https://github.com/aliyzd95/modified_shemo](https://github.com/aliyzd95/modified_shemo) provide audio files. Place the zip file named `shemo` in the `/data/shemo` directory of your project. You should also copy the `modified_shemo.json` file into the `data/shemo` directory of your project.

It should look like this:
data/ └── shemo/ ├── shemo/ └── modified_shemo.json


#### Iterative Approach To Finding A Model for Semantic Analytics
first we tried a simple lstm model which was doing pretty good and Tess dataset, but in shemo dataset it gave us accuracy around 66 percent, then we tried to use a more complex model with deeper layers and more complicated design, but the  accuracy decrease even more, in this process the importance of taking actions so our data can represent real world data was interesting, for example i saw that we could randomly make some of our samples paly faster or slower so we could avoid over fitting, any then i tried this pre trained model `superb/wav2vec2-base-superb-er`, it gave us accuracy around 50 percent, we tried to fine tune it with shemo data set but the ram resource was not enough, we tries to break dataset to partitions and train it every time and save it but during the training model forgot the previous patterns and the result got very bad, so we tried to fine tune the model with smaller number of data, and test it in rest of it, the result was pretty good and because the test dataset was considerably bigger than the train data set, we though its a good thing.
 