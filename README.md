# Android-Time-Hacks
This repository is made with the objective of reduce boring mandatory code of some of the most used elements of android

## GenericRecyclerAdapter
- Easy but little limited way to do your RecyclerView.Adapter. The objective here is to write the minimum code ammount to do a common adapter.

usage:

define your **ViewHolder**
``` java
    public class YourViewHolder extends RecyclerView.ViewHolder{

        //define your viewholder objects

        public YourViewHolder(View itemView) {
            super(itemView);
        }
    }
```

create an object of **GenericReclyclerAdapter** passing the right parameters, in this example, an list of String
``` java
    GenericRecyclerAdapter<String, YourViewHolder> genericRecyclerAdapter;
    genericRecyclerAdapter = new GenericRecyclerAdapter<>(this, strings, new GenericRecyclerAdapter.GenericRecyclerViewInterface<YourViewHolder>() {
        @Override
        public YourViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
            View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.your_layout, parent, false);
            return new YourViewHolder(view);
        }

        @Override
        public void onBindViewHolder(YourViewHolder holder, int position) {
            //bind your viewholder
        }
    });
    recyclerView.setAdapter(genericRecyclerAdapter);
```


## AndroidIdLinker
- Shortcut to link your views in xml to java code **(only tested on linux, can't link fragments or includes)**

usage:

just call **python android_id_linker.py** passing the right arguments

possible arguments:

**-h**: will show the options

**-a \<directory>**: will apply the code in the entire directory on files that ends with **.xml**

**-i \<file>**: will apply the code in the file

**-m \<modifier>**: will add a modifier in all the objects **(ex: private, public, ...)**

**-f \<fragment_view>**: use it if you want to call findViewById from a specific view **(ex: view.findViewById(...))**


usage example: **python android_id_linker.py -a ~/android_project/app/src/main/res/layout/ -o file.txt -m private -f view**

