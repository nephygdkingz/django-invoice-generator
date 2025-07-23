Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/focal64"
    config.vm.network "forwarded_port", guest: 8000, host: 8000
    config.vm.synced_folder ".", "/vagrant", exclude: "venv/"
  
    config.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y docker.io docker-compose
      usermod -aG docker vagrant
    SHELL
end