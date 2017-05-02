import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.ViewGroup;
import java.util.ArrayList;

/**
 * Created by Lucas on 02/05/2017.
 */

public class GenericRecyclerAdapter<L, V extends RecyclerView.ViewHolder> extends RecyclerView.Adapter<V>  {

    public ArrayList<L> list;
    public GenericRecyclerViewInterface<V> genericRecyclerViewInterface;
    public Context context;

    public GenericRecyclerAdapter(Context context, ArrayList<L> list, GenericRecyclerViewInterface<V> genericRecyclerViewInterface){
        this.list = list;
        this.genericRecyclerViewInterface = genericRecyclerViewInterface;
        this.context = context;
    }

    public ArrayList<L> getList(){
        return list;
    }

    public Context getContext(){
        return context;
    }

    @Override
    public V onCreateViewHolder(ViewGroup parent, int viewType) {
        return genericRecyclerViewInterface.onCreateViewHolder(parent, viewType);
    }

    @Override
    public void onBindViewHolder(V holder, int position) {
        genericRecyclerViewInterface.onBindViewHolder(holder, position);
    }

    @Override
    public int getItemCount() {
        return list.size();
    }

    public interface GenericRecyclerViewInterface<V>{
        public V onCreateViewHolder(ViewGroup parent, int viewType);
        public void onBindViewHolder(V holder, int position);
    }
}
