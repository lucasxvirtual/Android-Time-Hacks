import android.content.Context;
import android.content.SharedPreferences;

import static android.content.Context.MODE_PRIVATE;

/**
 * Created by Lucas on 06/11/2017.
 */

public class SharedPreferencesHelper {

    private final String PREF_ID = "APP_PREFERENCES";
    private SharedPreferences settings;
    private SharedPreferences.Editor editor;

    public SharedPreferencesHelper(Context context){
        settings = context.getSharedPreferences(PREF_ID, MODE_PRIVATE);
        editor = settings.edit();
    }

    public void putString(String key, String string){
        editor.putString(key, string);
        editor.apply();
    }

    public String getString(String key){
        return settings.getString(key, null);
    }

    public void erase(){
        editor.clear().apply();
    }
}
