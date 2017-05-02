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

