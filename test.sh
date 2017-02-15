fork do
	5.times do
	 sleep 1
         puts "I'm orphan"
       end
    end
abort "Parent process died"
