# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"

  # for selenium tests
  config.ssh.forward_x11 = true

  config.vm.network :forwarded_port, guest: 80, host: 6060

  config.vm.synced_folder ".", "/usr/local/otm/app/"

  if Vagrant::Util::Platform.windows? || Vagrant::Util::Platform.cygwin?
    config.vm.synced_folder ".", "/usr/local/otm/app/", type: "rsync", rsync__exclude: ["**/node_modules/", "**/.git", "opentreemap/"]
    config.vm.synced_folder "opentreemap/", "/usr/local/otm/app/opentreemap/"
  else
    config.vm.synced_folder ".", "/usr/local/otm/app/"
  end

  config.vm.provision :shell, :path => "scripts/bootstrap.sh"

  config.vm.provider :virtualbox do |vb, override|
    override.vm.box_url = "http://files.vagrantup.com/precise64.box"
    override.vm.provision :shell, :path => "scripts/virtualbox.sh"
    vb.customize ["modifyvm", :id, "--memory", 2048, "--cpus", "2"]
  end
  config.vm.provider :lxc do |lxc, override|
    override.vm.box_url = "http://bit.ly/vagrant-lxc-precise64-2013-07-12"
    override.vm.provision "shell", inline: "sudo apt-get install -qy python-apt"
    lxc.customize "cgroup.memory.limit_in_bytes", '2048M'
  end
end
