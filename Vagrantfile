Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.synced_folder ".", "/vagrant", exclude: "venv/"

    # Add or modify this block:
    config.vm.provider "virtualbox" do |vb|
      vb.memory = 2048   # 2GB
      vb.cpus = 2        # Optional: gives it more cores
    end
  
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io
      usermod -aG docker vagrant
    SHELL
end