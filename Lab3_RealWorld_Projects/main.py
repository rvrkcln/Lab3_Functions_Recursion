import access_control as ac
import media_engine as me

SEED_NUM = 0   
FAVORITE_ARTIST = "BLACKPINK" 


# 2. AUTOMATED CALCULATIONS
CONTROL_NUM = max(1, SEED_NUM) #
artist_len = len(FAVORITE_ARTIST)

print("--- ANSWERS FOR IMAGE 1 (Mission 1) ---")
access_lvl = CONTROL_NUM * 3 + artist_len #
threshold = CONTROL_NUM + 5 #
decision = ac.validate_access(access_lvl, threshold) #

print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Length: {artist_len}")
print(f"Computed Access Level: {access_lvl}")
print(f"Threshold Applied: {threshold}")
print(f"Final Authorization Decision: {decision}\n")

print("--- ANSWERS FOR IMAGE 2 (Mission 2) ---")
initial_pwr = CONTROL_NUM + artist_len #
print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"Initial Signal Strength: {initial_pwr}")
print(f"Base Case Condition: power == 0") #
total_calls = me.signal_shutdown(initial_pwr) #
print(f"Total Recursive Calls: {total_calls}\n")

print("--- ANSWERS FOR IMAGE 3 (Mission 3) ---")
stream_limit = CONTROL_NUM + artist_len #
play_counts = list(me.play_count_stream(stream_limit)) #

print(f"CONTROL_NUM Used: {CONTROL_NUM}")
print(f"FAVORITE_ARTIST Used: {FAVORITE_ARTIST}")
print(f"Computed Stream Limit: {stream_limit}")
print(f"Generated Play Counts: {play_counts}")
print(f"Total Plays: {sum(play_counts)}")
print(f"Number of Records Processed: {len(play_counts)}")